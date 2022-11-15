#include "rclcpp/rclcpp.hpp"
// 1. 导入消息类型 std_msgs/msg/String
#include "std_msgs/msg/string.hpp"
// 1a. 导入发布者的消息接口类型
#include "std_msgs/msg/u_int32.hpp"

// using std::placeholders::_1;

class SingleDogNode: public rclcpp::Node {
private:
  /*data*/
  // 3. 声明订阅者
  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr sub_novel;

  // 2a. 声明话题发布者
  rclcpp::Publisher<std_msgs::msg::UInt32>::SharedPtr pub_money;


  // 2. 创建订阅的回调函数
  void novel_callback(const std_msgs::msg::String::SharedPtr novels) {
    // 收到消息后发布逻辑
    std_msgs::msg::UInt32 money;
    money.data = 10;
    // 发布钱
    pub_money->publish(money);
 

    // 4. 编写回调逻辑
    RCLCPP_INFO(this->get_logger(),"我已经看了%s.",novels->data.c_str());
  }
public:
  SingleDogNode(std::string name):Node(name)
  {
    RCLCPP_INFO(this->get_logger(),"大家好，我是单身狗%s节点",name.c_str());
    // 5. 创建订阅者
    sub_novel = this->create_subscription<std_msgs::msg::String>("sexy_girl",10,std::bind(&SingleDogNode::novel_callback,this,std::placeholders::_1));
    // 3a. 创建话题的发布者
    pub_money = this->create_publisher<std_msgs::msg::UInt32>("sexy_girl_money",10);
  }
};

int main(int argc, char ** argv)
{
  rclcpp::init(argc,argv);
  auto node = std::make_shared<SingleDogNode>("wang2");
  rclcpp::spin(node);
  rclcpp::shutdown();
}