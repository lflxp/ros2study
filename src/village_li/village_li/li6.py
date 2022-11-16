import rclpy
from rclpy.node import Node
from std_msgs.msg import String,UInt32
# 1. 导入服务接口
from village_interfaces.srv import BorrowMoney

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
        self.timer_period = 5
        # 创建定时器
        self.timer = self.create_timer(self.timer_period,self.timer_callback)

        # 创建订阅者
        self.account = 80
        # 创建并初始化订阅者成员属性submoney
        self.submoney = self.create_subscription(UInt32,"sexy_girl_money",self.recv_money_callback,10)

        # 3. 声明并创建服务端
        self.borrow_server = self.create_service(BorrowMoney,"borrow_money",self.borrow_money_callback)

    # 2. 创建服务端的回调函数
    def borrow_money_callback(self,request,response):
        """
            4. 编写回调函数的逻辑处理请求
        """
        self.get_logger().info("borrow_money_callback")
        self.get_logger().info("收到来自：%s 的借钱请求，账户目前有: %d" % (request.name,self.account))
        if request.money <= self.account * 0.1:
            response.success = True
            response.money = request.money
            self.account = self.account - request.money
            self.get_logger().info("借钱成功，借出: %d,目前还剩 %d"  % (response.money,self.account))
        else:
            response.success = False
            response.money = 0
            self.get_logger().info("借钱失败,现在手头紧，不能借给你！")
        return response

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