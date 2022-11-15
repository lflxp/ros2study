import rclpy
from rclpy.node import Node
from std_msgs.msg import String,UInt32

# 白飘荡 
class Node07(Node):
    """
    创建一个Node04节点，并在初始化时输出一个话
    """
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("大家好，我是%s!" % name)

        # 创建订阅者
        # 创建并初始化订阅者成员属性submoney
        self.submoney = self.create_subscription(String,"sexy_girl",self.recv_sexy_girl_callback,10)

    def recv_sexy_girl_callback(self,novel):
        """
        发布者回调函数
        """
        self.get_logger().info("收到sexy_girl的书，里的内容是: %s" % novel.data)


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
    node = Node07("li7")  # 新建一个节点
    rclpy.spin(node) # 保持节点运行，检测是否收到退出指令（Ctrl+C）
    rclpy.shutdown() # 关闭rclpy