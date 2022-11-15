# py

操作命令

```
> mkdir -p town_ws/src && cd town_ws/src
> ros2 pkg create village_li --build-type ament_python --dependencies rclpy
> colcon build
> ros2 pkg list|grep village_li
> colcon build --packages-select village_li
> ros2 run village_li li6
> ros2 topic list
> ros2 topic info /sexy_girl_money
> ros2 topic pub /sexy_girl_money std_msgs/msg/UInt32 "{data: 20}" -1
> ros2 interface show std_msgs/msg/UInt32
```

# TODO

- https://www.bilibili.com/video/BV1gr4y1Q7j5?p=38&vd_source=d66d1a0aa1f1aea6a6386637292e894f

# cpp wanger扮演订阅渠道/sex_girl topic 然后通过发布渠道/sexy_girl_money进行付钱

操作命令

```
> ros2 pkg create village_wanger --build-type ament_cmake --dependencies rclcpp
```