import rclpy
from rclpy.node import Node
from std_msgs.msg import String,UInt32
# 1. 导入服务接口
from village_interfaces.srv import BorrowMoney

# service client 
class ServiceClient(Node):
    """
    创建一个Node04节点，并在初始化时输出一个话
    """
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("大家好，我是%s!" % name)

        # 创建订阅者
        # 创建并初始化订阅者成员属性submoney
        self.submoney = self.create_subscription(String,"sexy_girl",self.recv_sexy_girl_callback,10)
        # 3. 声明并创建接收逻辑
        self.borrow_money_client = self.create_client(BorrowMoney,"borrow_money")

    def recv_sexy_girl_callback(self,novel):
        """
        发布者回调函数
        """
        self.get_logger().info("收到sexy_girl的书，里的内容是: %s" % novel.data)

    # 2. 创建请求结果接收回调函数
    def borrow_response_callback(self,response):
        """
        借钱结果回调
        """
        # 4. 编写结果接收逻辑
        result = response.result()
        if result.success:
            self.get_logger().info("借到%d钱，去吃火锅!" % result.money)
        else:
            self.get_logger().info("连几块钱都不给，真扣门...")

    # 调用客户端发送请求
    def borrow_money_eat(self,money=10):
        self.get_logger().info("借钱吃火锅了，要借%d元" % money)
        # 确认服务是否在线，如果在线则跳出循环
        while not self.borrow_money_client.wait_for_service(1.0):
            self.get_logger().warn("服务不在线，我再等等看...")
        # 构造请求内容
        request = BorrowMoney.Request()
        request.name = self.get_name()
        request.money = money
        
        # 发送异步借钱请求
        self.borrow_money_client.call_async(request).add_done_callback(self.borrow_response_callback)


def main(args=None):
    """
    ros2运行该节点的入口函数
    编写ROS2节点的一般步骤
    1. 导入库文件
    2. 初始化客户端库
    3. 新建节点对象
    4. spin循环节点
    5. 关闭客户端库
    """
    rclpy.init(args=args) # 初始化rclpy
    node = ServiceClient("li8")  # 新建一个节点
    node.borrow_money_eat()
    rclpy.spin(node) # 保持节点运行，检测是否收到退出指令（Ctrl+C）
    rclpy.shutdown() # 关闭rclpy