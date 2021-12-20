#-*- coding:utf-8 -*-

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
from std_msgs.msg import String

moveit_commander.roscpp_initialize(sys.argv)
#rospy.init_node('move_group_python_interface_tutorial',anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()

group_name = "indy7"
move_group = moveit_commander.MoveGroupCommander(group_name)

planning_frame = move_group.get_planning_frame()

#object (banana)
os.system("rosrun gazebo_ros spawn_model -file /home/choi/catkin_ws/src/indy-ros/indy7_description/urdf/banana.xacro  -urdf -z 1 -x 0.5 -y 0.2 -P 1.57079 -model model")

transcript = String()
object_flag = 0

distance = 0

def set_position(num,voice2):

	waypoints = []
	waypoints.append(move_group.get_current_pose().pose)
	print(waypoints)

	wpose = geometry_msgs.msg.Pose()

	if num == 1:
		wpose=[0,-15*3.141592/180,-90*3.141592/180,0,-75*3.141592/180,0]
		move_group.go(wpose, wait=True)
		move_group.stop()

	if num == 2: #x-axis
		wpose.orientation.x = 1.0
		wpose.orientation.y = 0
		wpose.orientation.z = 0
		wpose.orientation.w = 0

		wpose.position.x = waypoints[0].position.x + voice2/10
		wpose.position.y = waypoints[0].position.y
		wpose.position.z = waypoints[0].position.z
		waypoints.append(copy.deepcopy(wpose))

		(plan, fraction) = move_group.compute_cartesian_path(waypoints, 0.01, 0.0)

		move_group.execute(plan, wait=True)
		move_group.stop()

	if num == 3: #y-axis
		wpose.orientation.x = 1.0
		wpose.orientation.y = 0
		wpose.orientation.z = 0
		wpose.orientation.w = 0

		wpose.position.x = waypoints[0].position.x
		wpose.position.y = waypoints[0].position.y + voice2/10
		wpose.position.z = waypoints[0].position.z
		waypoints.append(copy.deepcopy(wpose))

		(plan, fraction) = move_group.compute_cartesian_path(waypoints, 0.01, 0.0)

		move_group.execute(plan, wait=True)
		move_group.stop()

	if num == 4: #z-axis
		wpose.orientation.x = 1.0
		wpose.orientation.y = 0
		wpose.orientation.z = 0
		wpose.orientation.w = 0

		wpose.position.x = waypoints[0].position.x
		wpose.position.y = waypoints[0].position.y
		wpose.position.z = waypoints[0].position.z - voice2/10
		waypoints.append(copy.deepcopy(wpose))

		(plan, fraction) = move_group.compute_cartesian_path(waypoints, 0.01, 0.0)

		move_group.execute(plan, wait=True)
		move_group.stop()

	print("Waiting while RVIZ displays cartesian_path")

def callback(data):
	transcript = data.data

	transcript = transcript.split(' ')
	
	if transcript[0].find('ready') > -1:
		object_flag = 1
		print(object_flag)
		set_position(object_flag,0)

	if transcript[0].find('x') > -1 or transcript[0].find('X') > -1:
		object_flag = 2
		print(object_flag)
		set_position(object_flag,int(transcript[1]))

	if transcript[0].find('y') > -1 or transcript[0].find('Y') > -1:
		object_flag = 3
		print(object_flag)
		set_position(object_flag,int(transcript[1]))

	if transcript[0].find('z') > -1 or transcript[0].find('g') > -1 or transcript[0].find('\uC950') > -1:
		object_flag = 4
		print(object_flag)
		set_position(object_flag,int(transcript[1]))

rospy.init_node('VoiceControl',anonymous=True)
rospy.Subscriber('/Voice', String, callback)
rospy.spin()
