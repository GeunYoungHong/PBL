#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
from moveit_msgs.msg import MoveGroupActionResult
import geometry_msgs.msg
import shape_msgs.msg
from math import pi
from std_msgs.msg import String
import std_msgs.msg
from moveit_commander.conversions import pose_to_list, list_to_pose

class PickNPlaceTutorial():
    """PickNPlaceTutorial"""
    def __init__(self):
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('pick_n_place_tutorial', anonymous=True)

        self.scene = moveit_commander.PlanningSceneInterface()
        self.robot_group = moveit_commander.MoveGroupCommander('indy7')
        self.hand_group = moveit_commander.MoveGroupCommander('hand')

        self.plan_result_pub = rospy.Publisher("/move_group/result", MoveGroupActionResult, queue_size=1)

        # Misc variables
        self.box_name = ''

    def hold_hand(self, target_name):
        touch_links = ['left_inner_finger', 'right_inner_finger']
        self.hand_group.attach_object(target_name, 'robotiq_85_base_link', touch_links=touch_links)

    def release_hand(self, target_name):
        self.hand_group.detach_object(target_name)

    def jmove_to_pose_goal(self, pose_goal):
        # self.robot_group.set_pose_target(pose_goal)
        plan = self.robot_group.plan(pose_goal)
        self.robot_group.execute(plan, wait=True)
        # self.robot_group.go(wait=True)

    def jmove_to_joint_goal(self, joint_goal):
        # self.robot_group.go(joint_goal, wait=True)
        plan = self.robot_group.plan(joint_goal)
        self.robot_group.execute(plan, wait=True)
        
    def tmove_to_pose_goal(self, pose_goal):
        waypoints = []
        waypoints.append(self.robot_group.get_current_pose().pose)
        waypoints.append(pose_goal)

        plan, _ = self.robot_group.compute_cartesian_path(
                                   waypoints,   # waypoints to follow
                                   0.01,        # eef_step
                                   0.0)         # jump_threshold

        msg = MoveGroupActionResult()
        msg.result.planned_trajectory = plan
        self.plan_result_pub.publish(msg)
        self.robot_group.execute(plan)
    
    def wait_for_state_update(self, box_name, box_is_known=False, box_is_attached=False, timeout=4):
        start = rospy.get_time()
        seconds = rospy.get_time()
        while (seconds - start < timeout) and not rospy.is_shutdown():
            # Test if the box is in attached objects
            attached_objects = self.scene.get_attached_objects([box_name])
            is_attached = len(attached_objects.keys()) > 0

            # Note that attaching the box will remove it from known_objects
            is_known = box_name in self.scene.get_known_object_names()

            # Test if we are in the expected state
            if (box_is_attached == is_attached) and (box_is_known == is_known):
                return True

            rospy.sleep(0.1)
            seconds = rospy.get_time()
        return False

    def add_box(self, name, pose_stamp, size=(0.05, 0.05, 0.05)):
        self.scene.add_box(name, pose_stamp, size=size)
        self.wait_for_state_update(box_name=name, box_is_known=True)

def main():
    try:
        pnp = PickNPlaceTutorial()
        raw_input()

        table = geometry_msgs.msg.PoseStamped()
        table.header.frame_id = pnp.robot_group.get_planning_frame()
        table.pose.position.x =0.5
        table.pose.position.y =0
        table.pose.position.z =0.05
        table.pose.orientation.w = 1.0                           

        pnp.add_box(name='table', pose_stamp=table, size=(0.5, 0.5, 0.1))

        wall = geometry_msgs.msg.PoseStamped()
        wall.header.frame_id = pnp.robot_group.get_planning_frame()
        wall.pose.position.x =0.5
        wall.pose.position.y =0
        wall.pose.position.z =0.2
        wall.pose.orientation.w = 1.0                            

        pnp.add_box(name='wall', pose_stamp=wall, size=(0.01, 0.5, 0.25))

        cube_0 = geometry_msgs.msg.PoseStamped()
        cube_0.header.frame_id = pnp.robot_group.get_planning_frame()
        cube_0.pose.position.x =0.35
        cube_0.pose.position.y =-0.10
        cube_0.pose.position.z =0.13
        cube_0.pose.orientation.w = 1.0                            

        pnp.add_box(name='cube_0', pose_stamp=cube_0)

        cube_1 = geometry_msgs.msg.PoseStamped()
        cube_1.header.frame_id = pnp.robot_group.get_planning_frame()
        cube_1.pose.position.x =0.35
        cube_1.pose.position.y =0.10
        cube_1.pose.position.z =0.13
        cube_1.pose.orientation.w = 1.0                            

        pnp.add_box(name='cube_1', pose_stamp=cube_1)
        rospy.sleep(0.5)

        pnp.jmove_to_joint_goal([0, 0, -pi/2, 0, -pi/2, 0])

        pnp.jmove_to_pose_goal(list_to_pose([0.35, -0.10, 0.48, 0, -pi, -pi/2]))
        pnp.tmove_to_pose_goal(list_to_pose([0.35, -0.10, 0.18, 0, -pi, -pi/2]))
        pnp.hold_hand('cube_0')
        pnp.tmove_to_pose_goal(list_to_pose([0.35, -0.10, 0.28, 0, -pi, -pi/2]))

        pnp.jmove_to_pose_goal(list_to_pose([0.65, -0.10, 0.48, 0, -pi, -pi/2]))
        pnp.tmove_to_pose_goal(list_to_pose([0.65, -0.10, 0.18, 0, -pi, -pi/2]))
        pnp.release_hand('cube_0')
        pnp.tmove_to_pose_goal(list_to_pose([0.65, -0.10, 0.28, 0, -pi, -pi/2]))


        pnp.jmove_to_pose_goal(list_to_pose([0.35, 0.10, 0.48, 0, -pi, -pi/2]))
        pnp.tmove_to_pose_goal(list_to_pose([0.35, 0.10, 0.18, 0, -pi, -pi/2]))
        pnp.hold_hand('cube_1')
        pnp.tmove_to_pose_goal(list_to_pose([0.35, 0.10, 0.28, 0, -pi, -pi/2]))


        pnp.jmove_to_pose_goal(list_to_pose([0.65, 0.10, 0.48, 0, -pi, -pi/2]))
        pnp.tmove_to_pose_goal(list_to_pose([0.65, 0.10, 0.18, 0, -pi, -pi/2]))
        pnp.release_hand('cube_1')
        pnp.tmove_to_pose_goal(list_to_pose([0.65, 0.10, 0.28, 0, -pi, -pi/2]))

        pnp.jmove_to_joint_goal([0, 0, -pi/2, 0, -pi/2, 0])

    except rospy.ROSInterruptException:
        return
    except KeyboardInterrupt:
        return
    else:
        print("============ Python pick place demo complete!")
if __name__ == '__main__':
  main()
