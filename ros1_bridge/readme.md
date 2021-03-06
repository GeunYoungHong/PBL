# ROS1 bridge를 이용한 방법

* ROS1 bridge를 이용하여 ROS2 음성인식를 통해 ROS1 Gazebo 환경에서 Indy7를 조작하는 프로젝트 입니다.
```
git clone https://github.com/GeunYoungHong/PBL.git
```

![ROS1](https://user-images.githubusercontent.com/86825634/146858105-49798687-d251-4b7a-8533-6f5b16feb2c1.png)

## Dependency

- ROS1 bridge Install 
```
sudo apt install ros-noetic-ros1-bridge
```
- python3 voice recognition module Install 
```
pip3 install SpeechRecognition
```

## ROS1 build
```bash
cd PBL/ros1_bridge/
mv indy-ros/ ~/catkin_ws/src
mv control.py ~/catkin_ws/src

cd catkin_ws/
catkin_make
```

## ROS2 colcon build
```bash
cd PBL/ros2/
mv indy7_ign/ indy7_ign_moveit2/ indy7_moveit2_config/ rqt_example/ ~/robot_ws/src

cd robot_ws/
colcon build symlink-install
```

## Example

https://user-images.githubusercontent.com/86825634/146855955-2907f13e-a6ec-4f41-854e-0e97db5870b7.mp4

### Terminal 1 (ROS1 gazebo 실행)
```bash
cd ~/catkin_ws
source /opt/ros/noetic/setup.bash
source ~/catkin_ws/devel/setup.bash

roslaunch indy7_gazebo indy7_moveit_gazebo_table.launch
```

### Terminal 2 (ROS2 음성인식 실행)
```bash
cd ~/robot_ws
source /opt/ros/foxy/setup.bash
source ~/robot_ws/install/setup.bash

ros2 run rqt_example rqt_example
```

### Terminal 3 (ROS1 bridge 실행)
```bash
source /opt/ros/noetic/setup.bash
source /opt/ros/foxy/setup.bash

ros2 run ros1_bridge dynamic_bridge --bridge-all-topics
```

### Termianl 4 (Control 코드 실행)
```bash
cd ~/catkin_ws

python3 control.py
```
