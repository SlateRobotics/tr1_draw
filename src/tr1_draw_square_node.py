#!/usr/bin/env python

import sys
import time
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

rospy.sleep(1)
time.sleep(1)

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('tr1_draw_square_node', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("right_arm")

rospy.sleep(1)
time.sleep(1)

group.allow_replanning(True)
group.set_num_planning_attempts(5)
group.set_planning_time(5)
group.set_goal_orientation_tolerance(0.1)
group.set_goal_position_tolerance(0.1)

start_x = 0.500
start_y = 0.600
start_z = 0.800
square_size = 0.100

waypoints = []

wpose = geometry_msgs.msg.Pose()
wpose.orientation.w = 0.707
wpose.orientation.z = 0.707
wpose.position.x = start_x
wpose.position.y = start_y
wpose.position.z = start_z
waypoints.append(copy.deepcopy(wpose))

wpose.position.x = start_x
wpose.position.y = start_y + square_size
wpose.position.z = start_z
waypoints.append(copy.deepcopy(wpose))

wpose.position.x = start_x + square_size
wpose.position.y = start_y + square_size
wpose.position.z = start_z
waypoints.append(copy.deepcopy(wpose))

wpose.position.x = start_x + square_size
wpose.position.y = start_y
wpose.position.z = start_z
waypoints.append(copy.deepcopy(wpose))

wpose.position.x = start_x
wpose.position.y = start_y
wpose.position.z = start_z
waypoints.append(copy.deepcopy(wpose))

(plan, fraction) = group.compute_cartesian_path(waypoints, 0.01, 0.0)

group.execute(plan, wait=True)

