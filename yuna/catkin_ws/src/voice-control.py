import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

moveit_commander.roscpp_initialize(sys.argv)

rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "indy7"
group = moveit_commander.MoveGroupCommander(group_name)

display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                               moveit_msgs.msg.DisplayTrajectory,
                                               queue_size=20)

planning_frame = group.get_planning_frame()
eef_link = group.get_end_effector_link()
group_names = robot.get_group_names()
#print(robot.get_current_state())

while(1):
    voice1, voice2 = input('Input >> ').split()
    voice2 = int(voice2)

    pose_goal = geometry_msgs.msg.Pose()

    if voice1 == 'x' :
        pose_goal.position.x = 0.004859
        pose_goal.position.y = -0.196672
        pose_goal.position.z = 1.2668

        pose_goal.orientation.x = 0.0688
        pose_goal.orientation.y = 0.058196
        pose_goal.orientation.z = 2.387190
        pose_goal.orientation.w = 1.0

    if voice1 == 'y' :
        pose_goal.position.x = 0.1
        pose_goal.position.y = -0.2
        pose_goal.position.z = 1.3

        pose_goal.orientation.x = 0.0688
        pose_goal.orientation.y = 0.058196
        pose_goal.orientation.z = 2.387190
        pose_goal.orientation.w = 1.0

    if voice1 == 'z' :
        pose_goal.position.x = 0.004859
        pose_goal.position.y = -0.196672
        pose_goal.position.z = 1.2668

        pose_goal.orientation.x = 0.0688
        pose_goal.orientation.y = 0.058196
        pose_goal.orientation.z = 2.387190
        pose_goal.orientation.w = 1.0

    if voice1 == 'q' :
        pose_goal.position.x = 0.1
        pose_goal.position.y = -0.2
        pose_goal.position.z = 1.3

        pose_goal.orientation.x = 0.0688
        pose_goal.orientation.y = 0.058196
        pose_goal.orientation.z = 2.387190
        pose_goal.orientation.w = 1.0

    group.set_pose_target(pose_goal)
    plan = group.go(wait=True)
    group.stop()
