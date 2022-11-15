import rclpy
from rclpy.node import Node
from std_msgs.msg import String,UInt32

# https://fishros.com/d2lros2/#/humble/chapt3/get_started/3.%E8%AF%9D%E9%A2%98%E4%B9%8BRCLPY%E5%AE%9E%E7%8E%B0?id
# https://www.bilibili.com/video/BV1gr4y1Q7j5?p=33&spm_id_from=pageDriver&vd_source=d66d1a0aa1f1aea6a6386637292e894f
class Node06(Node):
    """
    创建一个Node04节点，并在初始化时输出一个话
    """
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("大家好，我是%s!" % name)
        # 创建发布者
        self.pub_novel = self.create_publisher(String,"sexy_girl",10)

        self.count = 0
        self.timer_period = 1
        # 创建定时器
        self.timer = self.create_timer(self.timer_period,self.timer_callback)

        # 创建订阅者
        self.account = 80
        # 创建并初始化订阅者成员属性submoney
        self.submoney = self.create_subscription(UInt32,"sexy_girl_money",self.recv_money_callback,10)

    def timer_callback(self):
        """
        定时回调函数
        """
        msg = String()
        msg.data = "Hello %d World! %d" % (self.count,self.count)
        self.pub_novel.publish(msg) 
        self.get_logger().info("发布了一个章节的小说，内容是：%s" % msg.data)
        self.count += 1

    def recv_money_callback(self,money):
        """
        发布者回调函数
        """
        self.account += money.data
        self.get_logger().info("收到%d的钱，账户里的钱%d" % (money.data,self.account))


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
    node = Node06("li6")  # 新建一个节点
    rclpy.spin(node) # 保持节点运行，检测是否收到退出指令（Ctrl+C）
    rclpy.shutdown() # 关闭rclpy