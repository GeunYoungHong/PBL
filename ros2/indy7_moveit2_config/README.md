# indy7_moveit2_config
ROS2 환경에서 MoveIt2 패키지를 이용하기 위한 Indy7의 configuration 파일들(yaml, srdf)을 포함하고 있습니다.

# 설치 및 확인
다음의 명령어를 통해 원격 저장소로부터 package를 내려받아 자신의 colcon workspace에 설치합니다.

```bash
mkdir -p ~/robot_ws/src # colcon workspace가 없을 경우만 수행합니다.
cd ~/robot_ws/src
git clone https://github.com/HYU-PBLRC-PB1/indy7_moveit2_config.git # 원격 저장소로부터 package를 다운로드합니다.
cd ~/robot_ws && colcon build --symlink-install # colcon workspace에서 빌드를 진행합니다.
```

# 패키지 구조
원격 저장소로부터 내려받은 패키지의 파일 구조를 확인하기 위해 다음의 명령어를 수행합니다.
```bash
cd ~/robot_ws/src/indy7_moveit2_config
tree
```

```bash
indy7_moveit2_config
├── CMakeLists.txt
├── config
│   ├── fake_control
│   │   ├── controllers.yaml
│   │   ├── indy7_arm_controller.yaml
│   │   └── start_position.yaml
│   ├── joint_limits.yaml # 관절의 joint acc, vel의 제한이 기록된 파일
│   ├── kinematics.yaml # 기구학 해석 library 지정
│   └── ompl_planning.yaml # 정의한 move_group별 역기구학 planner 지정
├── launch
│   ├── move_group_action_server.launch.py
│   ├── move_group_fake_control.launch.py
│   ├── rviz_interactive.rviz
│   └── rviz.rviz
├── LICENSE
├── package.xml
├── README.md
└── srdf
    ├── indy7_arm.srdf.xacro # indy7_arm.xacro를 단순 참조하는 srdf 파일 
    ├── indy7_arm.xacro # indy7의 base, end-effector link 정보, joint 정보, 무시할 collision 정보 등이 기록된 파일
    └── indy7.srdf # indy7_arm.srdf.xacro에서 macro를 해독한 파일로 xacro 패키지를 이용하여 생성한 파일
```