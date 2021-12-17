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

## 팁
private repository의 personal access token 인증 과정을 반복적으로 수행하지 않기 위해 다음의 명령어를 수행하는 것을 권장합니다.

```bash
git config --global credential.helper cache
git config --global credential.helper "cache --timeout=3600" # 인증한 token을 3600초 동안 cache  
```

## 설치 및 확인
다음의 명령어를 통해 원격 저장소로부터 package를 내려받아 자신의 colcon workspace에 설치합니다.

```bash
mkdir -p ~/robot_ws/src # colcon workspace가 없을 경우만 수행합니다.
cd ~/robot_ws/src
git clone https://github.com/HYU-PBLRC-PB1/indy7_ign_moveit2.git # 원격 저장소로부터 package를 다운로드합니다.
cd ~/robot_ws && colcon build --symlink-install # colcon workspace에서 빌드를 진행합니다.
source ~/robot_ws/install/setup.bash
```

## 패키지 구조
원격 저장소로부터 내려받은 패키지의 파일 구조를 확인하기 위해 다음의 명령어를 수행합니다.
```bash
cd ~/robot_ws/src/indy7_ign_moveit2
tree
```

```bash
indy7_ign_moveit2
├── CMakeLists.txt
├── examples
│   ├── cpp
│   │   └── example_ign_moveit2.cpp
│   └── python
│       ├── example_follow_object_direct.py
│       ├── example_follow_object.py
│       ├── example_follow_object_wait_until_executed.py
│       ├── example_gripper.py
│       ├── example_joint_goal.py
│       ├── example_pose_goal.py
│       └── example_throw.py
├── include
│   └── indy7_ign_moveit2
├── launch
│   ├── examples
│   │   ├── example_cpp.launch.py
│   │   ├── example_follow_object_direct.launch.py
│   │   ├── example_follow_object.launch.py
│   │   ├── example_follow_object_wait_until_executed.launch.py
│   │   ├── example_throw.launch.py
│   │   └── worlds
│   │       ├── world_indy7_follow.launch.py
│   │       └── world_indy7_throw.launch.py
│   ├── ign_moveit2.launch.py
│   └── rviz.rviz
├── LICENSE
├── moveit2_py
│   └── moveit2.py
├── package.xml
├── README.md
├── src
└── worlds
    ├── indy7_follow.sdf
    └── indy7_throw.sdf

```

## 예제1
기본적인 예제를 수행하기 위해 다음의 명령어를 실행합니다.
```bash
cd ~/robot_ws && source install/setup.bash
ros2 launch indy7_ign_moveit2 example_follow_object.launch.py
```
![fig1](figure/fig1.png)

Indy7이 MoveIt2 interface를 이용하여 목표를 잘 추종하는 지 확인하기 위해 목표(큐브)의 위치를 조작합니다.

* 실행된 Ignition Gazebo에서 우측 상단의 ⋮ 모양을 클릭합니다.
* Component inspector를 입력한 뒤 클릭합니다.
* Ignition world에 있는 큐브를 클릭합니다.
* Component inspector상의 Pose 정보를 변경합니다.

![fig2](figure/fig2.png)

예상되는 실행 결과는 다음 그림과 같습니다.
![example](figure/example.gif)

## 예제2





### Terminal 1
```bash
cd ~/robot_ws && source install/setup.bash
ros2 launch indy7_ign_moveit2 example_topic.launch.py 
```
### Terminal 2
```bash
ros2 topic pub --once /xyz_pose std_msgs/msg/String 'data: "-0.1 0.0 0.0"'
# wait for 5 seconds!
ros2 topic pub --once /xyz_pose std_msgs/msg/String 'data: "-0.1 0.0 0.0"'
# wait for 5 seconds!
ros2 topic pub --once /xyz_pose std_msgs/msg/String 'data: "0.1 0.0 0.0"'
```

### How does it work? (examples/python/example_topic.py)
```python
# base pose
self.latest_position = [0.25, 0.25, 0.25]
self.latest_quat = [1.0, 0.0, 0.0, 0.0]
```

```python
# msg.data = "-0.1, 0.0, 0.0"
# xyz_msg = ["-0.1", "0.0", "0.0"]
# xyz = [-0.1, 0.0, 0.0] 
xyz_msg = msg.data.split(' ')
xyz = [float(elem) for elem in xyz_msg]

self.latest_position[0] += xyz[0]       
self.latest_position[1] += xyz[1]
self.latest_position[2] += xyz[2]

self.moveit2_.set_pose_goal(self.latest_position, self.latest_quat)
# Plan and execute
self.moveit2_.plan_kinematic_path()
self.moveit2_.execute()
```

## 기타
현재 Ignition Gazebo에서 spawn이 되는 indy7의 model은 'Ignition Robotics'의 robot asset 공유 저장소인 [Fuel](https://app.ignitionrobotics.org/pmh5050/fuel/models/indy7)에서 다운로드 후 spawn이 수행되게끔 패키지 내에 구현되어 있습니다.

따라서, 원격 저장소([Fuel](https://app.ignitionrobotics.org/pmh5050/fuel/models/indy7))에서 변경사항이 있을 경우 이를 반영하기 위해선 local 장치에 설치되어 있는 indy7 model을 직접 삭제해주어야 합니다.

다음의 명령어를 통해 local 장치에 설치되어 있는 indy7 model을 제거할 수 있습니다. 
```bash
cd ~/.ignition/
rm -rf fuel
```
또는 다음의 경로에 직접 접근하는 방식으로 indy7의 model 파일(sdf)을 수정할 수 있습니다.
```
~/.ignition/fuel/fuel.ignitionrobotics.org/pmh5050/models/indy7
```
