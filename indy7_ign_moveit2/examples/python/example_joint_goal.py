#!/usr/bin/env python3

from moveit2 import MoveIt2Interface
import rclpy
import threading


def main(args=None):
    rclpy.init(args=args)

    # Initialise MoveIt2
    moveit2 = MoveIt2Interface()

    # Spin MoveIt2 node in the background
    executor = rclpy.executors.MultiThreadedExecutor(1)
    executor.add_node(moveit2)
    thread = threading.Thread(target=executor.spin)
    thread.start()

    # Set joint target to reach
    joint_positions = [1.57,
                       -1.57,
                       0.0,
                       0.0,
                       0.0,
                       0.0]
    moveit2.set_joint_goal(joint_positions)

    # Plan and execute
    moveit2.plan_kinematic_path()
    moveit2.execute()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
