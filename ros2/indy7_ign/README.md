# indy7_ign
ROS2 및 Ignition Gazebo 환경에서 indy7을 불러들이기 위한 model 파일(urdf, sdf)을 포함하고 있습니다.

<!--
![indy7](indy7/thumbnails/1.png)
-->
indy7의 각 link의 좌표계 및 위치는 다음 그림과 같습니다.

![example2](figure/robot_model.png)

# 설치 및 확인
다음의 명령어를 통해 원격 저장소로부터 package를 내려받아 자신의 colcon workspace에 설치합니다.

```bash
mkdir -p ~/robot_ws/src # colcon workspace가 없을 경우만 수행합니다.
cd ~/robot_ws/src
git clone https://github.com/HYU-PBLRC-PB1/indy7_ign.git # 원격 저장소로부터 package를 다운로드합니다.
cd ~/robot_ws && colcon build --symlink-install # colcon workspace에서 빌드를 진행합니다.
```

# 예제
indy7의 configuration을 확인하기 위해 'joint_state_publisher_gui' node를 이용하는 예제에 해당합니다.
```bash
source ~/robot_ws/install/setup.bash
ros2 launch indy7_ign indy7_display.launch.py
```
각 joint angle 값을 직접 기록하거나 슬라이더를 이동시키면서 indy7 자세의 변화를 확인할 수 있습니다.

![example1](figure/joint_state_publisher_gui.png)
(* 그림과 같이 특정 link의 좌표계를 확인하고 싶은 경우 rviz2상에서 Show Axes 옵션을 활성화 합니다.)

## 오류 관련
만약 'joint-state-publisher-gui' 패키지를 찾을 수 없다는 오류가 발생한 경우 다음의 명령어를 실행한 뒤 다시 시도합니다.
```bash
# joint-state-publisher-gui 패키지가 설치되어있지 않은 경우
sudo apt-get install ros-foxy-joint-state-publisher-gui
ros2 launch indy7_ign indy7_display.launch.py
```

# 패키지 구조
원격 저장소로부터 내려받은 패키지의 파일 구조를 확인하기 위해 다음의 명령어를 수행합니다.
```bash
cd ~/robot_ws/src/indy7_ign
tree
```

```bash
indy7_ign
├── CMakeLists.txt
├── indy7
│   ├── meshes # urdf 및 sdf에서 참조하는 mesh 파일
│   │   ├── collision
│   │   │   ├── link0.stl
│   │   │   ├── link1.stl
│   │   │   ├── link2.stl
│   │   │   ├── link3.stl
│   │   │   ├── link4.stl
│   │   │   ├── link5.stl
│   │   │   └── link6.stl
│   │   └── visual
│   │       ├── link0.stl
│   │       ├── link1.stl
│   │       ├── link2.stl
│   │       ├── link3.stl
│   │       ├── link4.stl
│   │       ├── link5.stl
│   │       └── link6.stl
│   ├── model.config # Ignition model meta file
│   ├── model.sdf # SDF description of the indy7
│   └── thumbnails
│       └── 1.png
├── LICENSE
├── package.xml
├── README.md
├── scripts
│   ├── estimate_inertial_properties.py
│   └── indy7_inertial_out.sdf
└── urdf
    └── indy7.urdf
```