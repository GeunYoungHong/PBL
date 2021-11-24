#!/usr/bin/python

import sys
import os
import math

from time import sleep
from std_msgs.msg import Bool
from sensor_msgs.msg import JointState
import rospy

def rads2degs(rad_list):
    degs = [math.degrees(rad) for rad in rad_list]
    return degs

def degs2rads(deg_list):
    rads = [math.radians(deg) for deg in deg_list]
    return rads

class JointControllerApp():
    def __init__(self):
        rospy.init_node("joint_controller")

        self.execute_joint_state_pub = rospy.Publisher("/indy/execute_joint_state", JointState, queue_size=1)
        self.stop_pub = rospy.Publisher("/stop_motion", Bool, queue_size=1)

    def go(self, q):
        joint_state_msg = JointState()
        joint_state_msg.header.stamp = rospy.Time.now()
        joint_state_msg.name = ['joint0', 'joint1', 'joint2', 'joint3', 'joint4', 'joint5']
        joint_state_msg.position = degs2rads(q)
        joint_state_msg.velocity = []
        joint_state_msg.effort = []
        self.execute_joint_state_pub.publish(joint_state_msg)

    def stop(self):
        self.stop_pub.publish(True)

if __name__ == "__main__":
    app = JointControllerApp()
    
    while True:
        try:
            q = [0, 0, 0, 0, 0, 0]

            for i in range(6):
                q[i] = float(raw_input('query joint {} position '.format(i)))

            print('joint query : ' + str(q))

            go_sign = raw_input('enter g to move robot else to cancel')
            if go_sign == 'g':
                app.go(q)
            else:
                continue
            
            stop_sign = raw_input('enter s to move robot ')
            if stop_sign == 's':
                app.stop()
            else:
                continue

            exit_sign = raw_input('enter q to quit program ')
            if exit_sign == 'q':
                break
            else:
                continue

        except KeyboardInterrupt:
            sys.exit()
       
        
    