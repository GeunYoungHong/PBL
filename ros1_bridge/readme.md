## ROS1 bridge를 이용한 방법

* ROS1 bridge를 이용하여 ROS2 음성인식를 통해 ROS1 Gazebo 환경에서 Indy7를 조작하는 프로젝트 입니다.

## Dependency

- ROS1 bridge Install 
```
sudo apt install ros-noetic-ros1-bridge
```

## ROS2 colcon build
```
mkdir -p robot_ws/src
git clone https://github.com/GeunYoungHong/PBL.git
cd ..
colcon build symlink-install
```

## Example

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
ros2 topic echo /xyz_pose
```
### Termianl 4 (if needed to check indy7 is working or not in ros2)
```
cd ~/robot_ws && source ~/robot_ws/install/setup.bash
ros2 topic pub --once /xyz_pose std_msgs/msg/String 'data: "x 1"' # move to x-axis by 1cm
# wait for 5 seconds!
ros2 topic pub --once /xyz_pose std_msgs/msg/String 'data: "y 2"' # move to y-axis by 1cm
# wait for 5 seconds!
ros2 topic pub --once /xyz_pose std_msgs/msg/String 'data: "j nu"' # move to initial job position
```
