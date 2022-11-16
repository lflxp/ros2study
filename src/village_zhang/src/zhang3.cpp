#include "rclcpp/rclcpp.hpp"
#include "village_interfaces/srv/sell_novel.hpp"

// using std::placeholders::_1;

class PoorManNode: public rclcpp::Node {
public:
  PoorManNode(std::string name):Node(name)
  {
    RCLCPP_INFO(this->get_logger(),"大家好，我是张三狗%s节点",name.c_str());
    // 声明和创建客户端
    novel_client = this->create_client<village_interfaces::srv::SellNovel>("sell_novel");
  }

  // 编写发送请求逻辑
  void buy_novels() {
    RCLCPP_INFO(this->get_logger(),"准备去买小说了");
    // 1. 等待服务上线
    while (!novel_client->wait_for_service(std::chrono::seconds(1)))
    {
      RCLCPP_WARN(this->get_logger(), "等待服务端上线");
    }
    // 2. 构造请求数据
    auto request = std::make_shared<village_interfaces::srv::SellNovel_Request>();
    request->money = 5;
    // 3. 发送异步请求
    novel_client->async_send_request(request,std::bind(&PoorManNode::novels_callback,this,std::placeholders::_1));
  }

private:
  rclcpp::Client<village_interfaces::srv::SellNovel>::SharedPtr novel_client;

  // 编写接收小说结果的回调函数
  void novels_callback(rclcpp::Client<village_interfaces::srv::SellNovel>::SharedFuture response)
  {
    auto result = response.get();
    RCLCPP_INFO(this->get_logger(), "收到了%d章的小说，现在按章节读", result->novels.size());

    for(std::string novel:result->novels)
    {
      // 打印每一章节的小说内容
      RCLCPP_INFO(this->get_logger(), "%s", novel.c_str());
    }

    RCLCPP_INFO(this->get_logger(),"小说读完了，好刺激，写的真不错，价格经济实惠～");
  }
};

int main(int argc, char ** argv)
{
  rclcpp::init(argc,argv);
  auto node = std::make_shared<PoorManNode>("zhang3");
  node->buy_novels();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}