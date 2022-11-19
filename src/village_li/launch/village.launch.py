# 1. 导入包
from launch import LaunchDescription
from launch_ros.actions import Node

# 2. 定义函数名
def generate_launch_description():
  # 3. 创建节点描述
  li6_node = Node(
    package='village_li',
    executable='li6',
    # namespace='mirror',
    output='screen',
    parameters=[{'writer_timer_period': 1}]
  )
  li7_node = Node(
    package='village_li',
    executable='li7',
  )
  li8_node = Node(
    package='village_li',
    executable='li8',
  )
  wanger_node = Node(
    package="village_wanger",
    executable="wang2",
  )
  zhang_node = Node(
    package="village_zhang",
    executable="zhang3_node",
  )

  launch_description = LaunchDescription([li6_node,wanger_node,zhang_node,li7_node,li8_node])
  return launch_description

