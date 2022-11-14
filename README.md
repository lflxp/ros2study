# py

> mkdir -p town_ws/src && cd town_ws/src
> ros2 pkg create village_li --build-type ament_python --dependencies rclpy
> colcon build
> ros2 pkg list|grep village_li
> colcon build --packages-select village_li
> ros2 run village_li li6
> ros2 topic list
> ros2 topic info /sexy_girl_money
> ros2 topic pub /sexy_girl_money std_msgs/msg/UInt32 "{data: 20}" -1