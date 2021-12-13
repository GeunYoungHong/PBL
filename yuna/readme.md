## Indy7 Control using Voice Recognition

### ROS1 실행
```
cd PBL/catkin_ws
source /opt/ros/noetic/setup.bash 
source ~/catkin_ws/devel/setup.bash 
catkin_make 
```

### ROS2 실행
```
cd PBL/robot_ws
source /opt/ros/foxy/setup.bash 
source ~/robot_ws/install/local_setup.bash 
colcon build 
```

### ROS1 - ROS2 bridge 설치
```
sudo apt install ros-noetic-ros1-bridge
```

### Terminal 1 (gazebo 실행)
```
source /opt/ros/noetic/setup.bash
source ~/catkin_ws/devel/setup.bash 
roslaunch indy7_gazebo indy7_moveit_gazebo.table.launch 
```

### Terminal 2 (음성 인식 실행)
```
source /opt/ros/foxy/setup.bash 
source ~/robot_ws/install/local_setup.bash 
ros2 run rqt_example rqt_example 
```

### Terminal 3 (bridge 실행)
```
source /opt/ros/foxy/setup.bash 
source /opt/ros/noetic/setup.bash 
ros2 run ros1_bridge dynamic_bridge –bridge-all-topics 
```

### Terminal 4 (Control Code 실행)
```
cd catkin_ws 
python3 control.py 
```
