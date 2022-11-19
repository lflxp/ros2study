# 1. 导入包
from launch import LaunchDescription
from launch_ros.actions import Node

# 2. 定义函数名
def generate_launch_description():
  # 3. 创建节点描述
  li6_node = Node(
    package='village_li',
    executable='li6',
  )
  wanger_node = Node(
    package="village_wanger",
    executable="wang2",
  )
  zhang_node = Node(
    package="village_zhang",
    executable="zhang3_node",
  )

  launch_description = LaunchDescription([li6_node,wanger_node,zhang_node])
  return launch_description

