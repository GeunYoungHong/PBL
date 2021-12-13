#1. rosrun gazebo_ros spawn_model -file /home/choi/catkin_ws/src/indy-ros/indy7_description/urdf/banana.xacro  -urdf -z 1 -x 0.5 -y 0.2 -P 1.57079 -model model

#2. rosrun gazebo_ros spawn_model -file /home/choi/catkin_ws/src/indy-ros/indy7_description/urdf/drill.xacro  -urdf -z 1 -x 0.4 -y -0.2 -P 1.57079 -model model

#3. rosrun gazebo_ros spawn_model -file /home/choi/catkin_ws/src/indy-ros/indy7_description/urdf/bottle.xacro  -urdf -z 1 -x 0.7 -P 3.12 -model model

import sys
import os
import time
import copy

import pybullet as p
import signal
import numpy as np
import rospy

import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

from pybullet import getQuaternionFromEuler,getEulerFromQuaternion,getMatrixFromQuaternion
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

moveit_commander.roscpp_initialize(sys.argv)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()

group_name = "indy7"
move_group = moveit_commander.MoveGroupCommander(group_name)

planning_frame = move_group.get_planning_frame()

transcript = String()
object_flag = 0

def set_position(num):

	pose_goal = geometry_msgs.msg.Pose()

	if num == 1: #home
		print("1")
		pose_goal=[0,-15*3.141592/180,-90*3.141592/180,0,-75*3.141592/180,0]
		move_group.go(pose_goal, wait=True)
		move_group.stop()

	if num == 2: #banana
		print("2")
		pose_goal.orientation.x = 1.0
		pose_goal.orientation.y = 0
		pose_goal.orientation.z = 0
		pose_goal.orientation.w = 0

		pose_goal.position.x = 0.499971
		pose_goal.position.y = 0.200016
		pose_goal.position.z = 0.39
		move_group.set_pose_target(pose_goal)

		plan = move_group.go(wait=True)
		move_group.stop()

	if num == 3: #drill
		print("3")
		pose_goal.orientation.x = 1.0
		pose_goal.orientation.y = 0
		pose_goal.orientation.z = 0
		pose_goal.orientation.w = 0

		pose_goal.position.x = 0.400078
		pose_goal.position.y = -0.199972
		pose_goal.position.z = 0.45
		move_group.set_pose_target(pose_goal)

		plan = move_group.go(wait=True)
		move_group.stop()

	if num == 4: #bottle
		print("4")
		pose_goal.orientation.x = 1.0
		pose_goal.orientation.y = 0
		pose_goal.orientation.z = 0
		pose_goal.orientation.w = 0

		pose_goal.position.x = 0.67
		pose_goal.position.y = 0.000025
		pose_goal.position.z = 0.45
		move_group.set_pose_target(pose_goal)

		plan = move_group.go(wait=True)
		move_group.stop()


def callback(data):
	transcript = data.data

	if transcript.find('home') > -1:
		object_flag = 1
		set_position(1)

	if transcript.find('banana') > -1:
		object_flag = 2
		set_position(2)

	if transcript.find('drill') > -1:
		object_flag = 3
		set_position(3)

	if transcript.find('yellow') > -1:
		object_flag = 4
		set_position(4)

rospy.init_node('VoiceControl',anonymous=True)
rospy.Subscriber('/Voice', String, callback)
rospy.spin()
