# py

操作命令

```
> mkdir -p town_ws/src && cd town_ws/src
> ros2 pkg create village_li --build-type ament_python --dependencies rclpy
> colcon build
> ros2 pkg list|grep village_li
> colcon build --packages-select village_li
> source install/setup.zsh
> ros2 run village_li li6
> ros2 topic list
> ros2 topic info /sexy_girl_money
> ros2 topic pub /sexy_girl_money std_msgs/msg/UInt32 "{data: 20}" -1
> ros2 interface show std_msgs/msg/UInt32
> ros2 interface proto std_msgs/msg/UInt32
> ros2 interface package sensor_msgs
> ros2 interface list 
```

# TODO

- https://www.bilibili.com/video/BV1gr4y1Q7j5?p=38&vd_source=d66d1a0aa1f1aea6a6386637292e894f

# cpp wanger扮演订阅渠道/sex_girl topic 然后通过发布渠道/sexy_girl_money进行付钱

操作命令

```
> ros2 pkg create village_wanger --build-type ament_cmake --dependencies rclcpp
# 自定义消息
> ros2 pkg create village_interfaces --build-type ament_cmake
> colcon build --packages-select village_interfaces
> ros2 interface package village_interfaces
> ros2 interface show village_interfaces/msg/Novel
> ros2 interface proto village_interfaces/msg/Novel
```

# service

```
ros2 run examples_rclpy_minimal_service service
ros2 service list
ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts "{a: 5,b: 3}"
rqt
# 查看服务接口类型
ros2 service type /add_two_ints
ros2 interface show example_interfaces/srv/AddTwoInts
ros2 interface proto example_interfaces/srv/AddTwoInts
# 查看使用某一接口的服务
ros2 service find example_interfaces/srv/AddTwoInts
ros2 interface show village_interfaces/srv/BorrowMoney
ros2 interface show village_interfaces/srv/SellNovel 
ros2 interface package village_interfaces
https://www.bilibili.com/video/BV1gr4y1Q7j5/?p=46&spm_id_from=pageDriver&vd_source=d66d1a0aa1f1aea6a6386637292e894f
RMW_IMPLEMENTATION=rmw_cyclonedds_cpp ros2 run village_li li7
ros2 service list -t
ros2 run village_li li6
ros2 service call /borrow_money village_interfaces/srv/BorrowMoney "{name: 'fishros', money: 5}"
rqt
```

# c++ service client

```
ros2 pkg create village_zhang --build-type ament_cmake --dependencies rclcpp
colcon build
ros2 run village_zhang zhang3_node
ros2 run village_wanger wang2
ros2 run village_li li6
```

# param 参数

> https://www.bilibili.com/video/BV1gr4y1Q7j5?p=60&spm_id_from=pageDriver&vd_source=d66d1a0aa1f1aea6a6386637292e894f

```
ros2 param list
ros2 param list /li6
ros2 param get /li6 writer_timer_period
ros2 param set /li6 writer_timer_period 1
ros2 topic hz /sexy_girl
```