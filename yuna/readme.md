## Indy7 Control using Voice Recognition

# ROS1 실행
$ cd PBL/catkin_ws \n
$ \n
$ source /opt/ros/noetic/setup.bash \n
$ source ~/catkin_ws/devel/setup.bash \n
$ \n
$ catkin_make \n

# ROS2 실행
$ cd PBL/robot_ws \n
$ \n
$ source /opt/ros/foxy/setup.bash \n
$ source ~/robot_ws/install/local_setup.bash \n
$ \n
$ colcon build \n

# ROS1 - ROS2 bridge 설치
$ sudo apt install ros-noetic-ros1-bridge \n

# Terminal 1 (gazebo 실행)
$ source /opt/ros/noetic/setup.bash \n
$ source ~/catkin_ws/devel/setup.bash \n
$ \n
$ roslaunch indy7_gazebo indy7_moveit_gazebo.table.launch \n

# Terminal 2 (음성 인식 실행)
$ source /opt/ros/foxy/setup.bash \n
$ source ~/robot_ws/install/local_setup.bash \n
$ \n
$ ros2 run rqt_example rqt_example \n

# Terminal 3 (bridge 실행)
$ source /opt/ros/foxy/setup.bash \n
$ source /opt/ros/noetic/setup.bash \n
$ \n
$ ros2 run ros1_bridge dynamic_bridge –bridge-all-topics \n

# Terminal 4 (Control Code 실행)
$ cd catkin_ws \n
$ python3 control.py \n
