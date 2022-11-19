#include "rclcpp/rclcpp.hpp"
// 1. 导入消息类型 std_msgs/msg/String
#include "std_msgs/msg/string.hpp"
// 1a. 导入发布者的消息接口类型
#include "std_msgs/msg/u_int32.hpp"
// 1b. 导入服务接口
#include "village_interfaces/srv/sell_novel.hpp"
#include <queue>

// using std::placeholders::_1;

class SingleDogNode: public rclcpp::Node {
private:
  /*data*/
  // 3. 声明订阅者
  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr sub_novel;

  // 2a. 声明话题发布者
  rclcpp::Publisher<std_msgs::msg::UInt32>::SharedPtr pub_money;

  // 书库
  std::queue<std::string> novels_queue;

  // 声明单价为一元钱一张
  unsigned int novel_price = 1;

  // 声明回调组
  rclcpp::CallbackGroup::SharedPtr sell_novels_callback_group;

  // 声明服务端
  rclcpp::Service<village_interfaces::srv::SellNovel>::SharedPtr sell_server;

  // 2. 创建订阅的回调函数
  void novel_callback(const std_msgs::msg::String::SharedPtr novels) {
    // 收到消息后发布逻辑
    std_msgs::msg::UInt32 money;
    money.data = 10;
    // 发布钱
    pub_money->publish(money);
 
    // 把受到的小说放到书库里 
    novels_queue.push(novels->data);

    // 4. 编写回调逻辑
    RCLCPP_INFO(this->get_logger(),"我已经看了%s.",novels->data.c_str());
  }

  // 2b. 创建买书请求回调函数
  void sell_novel_callback(const village_interfaces::srv::SellNovel::Request::SharedPtr request,
                           const village_interfaces::srv::SellNovel::Response::SharedPtr response)
  {
    // 判断当前的书章节数量够不够，不够就要攒书，再返回
    // 等待novels_queue书库里的书的数量达到我们要卖出去的
    // 等待会让当前的线程阻塞
    RCLCPP_INFO(this->get_logger(),"收到一个买书的请求，一共给了%d元",request->money);

    this->get_parameter("novel_price",novel_price);
    // 计算应该返回给客户端的小说数量
    // unsigned int num = (int)request->money/(1.0);
    unsigned int num = (int)request->money/(novel_price);

    if(num > novels_queue.size())
    {
      // 等待，凑齐书
      RCLCPP_INFO(this->get_logger(),"等待,书不够, 书库%d 要卖出去 %d",novels_queue.size(),num);
    
      rclcpp::Rate rate(1);
      
      while (novels_queue.size() < num)
      {
        RCLCPP_INFO(this->get_logger(),"等待中，目前还差%d的小说",num-novels_queue.size());
        rate.sleep();
      }
      
    }
    RCLCPP_INFO(this->get_logger(),"当前书库里的书有%d，已经大于要卖出去的书的数量%d",novels_queue.size(),num);
    for(int i=0;i<(int)num;i++) {
      response->novels.push_back(novels_queue.front());
      novels_queue.pop();
    }
  }
public:
  SingleDogNode(std::string name):Node(name)
  {
    RCLCPP_INFO(this->get_logger(),"大家好，我是单身狗%s节点",name.c_str());
    // 5. 创建订阅者
    sub_novel = this->create_subscription<std_msgs::msg::String>("sexy_girl",10,std::bind(&SingleDogNode::novel_callback,this,std::placeholders::_1));
    // 3a. 创建话题的发布者
    pub_money = this->create_publisher<std_msgs::msg::UInt32>("sexy_girl_money",10);
    // 声明并创建服务端，同时自定义回调组
    sell_novels_callback_group = this->create_callback_group(rclcpp::CallbackGroupType::MutuallyExclusive);
    sell_server = this->create_service<village_interfaces::srv::SellNovel>("sell_novel",
                                                                            std::bind(&SingleDogNode::sell_novel_callback,this,std::placeholders::_1,std::placeholders::_2),
                                                                            rmw_qos_profile_services_default,
                                                                            sell_novels_callback_group);

    this->declare_parameter<std::int64_t>("novel_price", novel_price);
  }
};

int main(int argc, char ** argv)
{
  rclcpp::init(argc,argv);
  auto node = std::make_shared<SingleDogNode>("wang2");
  rclcpp::executors::MultiThreadedExecutor executor;

  // 多线程改造
  executor.add_node(node);
  executor.spin();

  // rclcpp::spin(node);
  rclcpp::shutdown();
}