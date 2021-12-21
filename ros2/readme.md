# ROS2를 이용한 방법
* PBL 1조의 코드를 참고해서 작성되었습니다.
* MoveIt2 interface를 이용하여 Ignition Gazebo 환경에서 Indy7를 조작하는 프로젝트 입니다.
```
git clone https://github.com/GeunYoungHong/PBL.git
```

## Dependency

- [ROS2 Foxy](https://docs.ros.org/en/foxy/Installation.html)
- [Ignition Fortress](https://ignitionrobotics.org/docs/fortress)
- [MoveIt 2](https://moveit.ros.org/)
  - [Binary Install](https://moveit.ros.org/install-moveit2/binary)
  - [Source Build(권장)](https://moveit.ros.org/install-moveit2/source/)
- [ros_ign](https://github.com/ignitionrobotics/ros_ign/tree/ros2)
- Ignition package for indy7
  - [indy7_ign](https://github.com/HYU-PBLRC-PB1/indy7_ign.git)
  - [indy7_moveit2_config](https://github.com/HYU-PBLRC-PB1/indy7_moveit2_config.git)

## ROS2 colcon build
```bash
cd PBL/ros2/
mv indy7_ign/ indy7_ign_moveit2/ indy7_moveit2_config/ rqt_example/ ~/robot_ws/src

cd robot_ws/
colcon build symlink-install
```

## Example

https://user-images.githubusercontent.com/86825634/146856658-45631a07-03dd-4859-89b9-b5fa214e719b.mp4 
https://user-images.githubusercontent.com/86825634/146856663-c6b6abb9-f96d-4990-9522-090bc54687ee.mp4

### Terminal 1
```bash
cd ~/robot_ws && source install/setup.bash
ros2 launch indy7_ign_moveit2 example_topic.launch.py 
```
### Terminal 2
```bash
cd ~/robot_ws && source ~/robot_ws/install/setup.bash
ros2 run rqt_example rqt_example
```
### Terminal 3 (check publisher between voice recognition and indy7)
```bash
cd ~/robot_ws && source ~/robot_ws/install/setup.bash
ros2 topic echo /Voice
```
### Termianl 4 (if needed to check indy7 is working or not in ros2)
```bash
cd ~/robot_ws && source ~/robot_ws/install/setup.bash

ros2 topic pub --once /Voice std_msgs/msg/String 'data: "x 1"' # move to x-axis by 1cm
# wait for 5 seconds!
ros2 topic pub --once /Voice std_msgs/msg/String 'data: "y 2"' # move to y-axis by 1cm
# wait for 5 seconds!
ros2 topic pub --once /Voice std_msgs/msg/String 'data: "j nu"' # move to initial job position
```
