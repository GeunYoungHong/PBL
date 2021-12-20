## PBL 1조의 코드를 참고해서 작성되었습니다.
https://github.com/HYU-PBLRC-PB1

# indy7_ign_moveit2
MoveIt2 interface를 이용하여 Ignition Gazebo 환경에서 Indy7를 조작하는 기초 프로젝트에 해당합니다.

## 의존성
- [ROS2 Foxy](https://docs.ros.org/en/foxy/Installation.html)
- [Ignition Fortress](https://ignitionrobotics.org/docs/fortress)
- [MoveIt 2](https://moveit.ros.org/)
  - [Binary Install](https://moveit.ros.org/install-moveit2/binary)
  - [Source Build(권장)](https://moveit.ros.org/install-moveit2/source/)
- [ros_ign](https://github.com/ignitionrobotics/ros_ign/tree/ros2)
- Ignition package for indy7
  - [indy7_ign](https://github.com/HYU-PBLRC-PB1/indy7_ign.git)
  - [indy7_moveit2_config](https://github.com/HYU-PBLRC-PB1/indy7_moveit2_config.git)

## ROS2 환경에서 voice recognition으로 indy7의 position teaching 구현 코드 colcon build
```
mkdir -p robot_ws/src
git clone git@github.com:GeunYoungHong/PBL -b ros_2
cd robot_ws
colcon build symlink-install
```

## 예제
### Terminal 1
```bash
cd ~/robot_ws && source install/setup.bash
ros2 launch indy7_ign_moveit2 example_topic.launch.py 
```
## Terminal 2
```bash
cd ~/robot_ws && source ~/robot_ws/install/setup.bash
ros2 run rqt_example rqt_example
```
## Terminal 3 (check publisher between voice recognition and indy7)
```bash
cd ~/robot_ws && source ~/robot_ws/install/setup.bash
ros2 topic echo /xyz_pose
```
## Termianl 4 (if needed to check indy7 is working or not in ros2)
```
cd ~/robot_ws && source ~/robot_ws/install/setup.bash
ros2 topic pub --once /xyz_pose std_msgs/msg/String 'data: "x 1"' # move to x-axis by 1cm
# wait for 5 seconds!
ros2 topic pub --once /xyz_pose std_msgs/msg/String 'data: "y 2"' # move to y-axis by 1cm
# wait for 5 seconds!
ros2 topic pub --once /xyz_pose std_msgs/msg/String 'data: "j nu"' # move to initial job position
```