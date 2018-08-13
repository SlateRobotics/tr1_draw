#!/usr/bin/env python

import sys
import time
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import math
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

rospy.sleep(1)
time.sleep(1)

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('tr1_draw_circle_node', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("right_arm")

rospy.sleep(1)
time.sleep(1)

group.set_goal_orientation_tolerance(0.5)
group.set_goal_position_tolerance(0.1)

waypoints = []

start_x = 0.600
start_y = 0.650
start_z = 0.700
circle_radius = 0.200

wpose = geometry_msgs.msg.Pose()
wpose.orientation.w = 0.707
wpose.orientation.z = 0.707
wpose.position.x = start_x
wpose.position.y = start_y
wpose.position.z = start_z
waypoints.append(copy.deepcopy(wpose))

iterations = 25
for i in range(iterations):
	theta = i * 1.0 / iterations * 1.0 * 6.283185
	wpose.position.x = start_x + (circle_radius * math.sin(theta))
	wpose.position.y = start_y + (circle_radius * math.cos(theta))
	waypoints.append(copy.deepcopy(wpose))

wpose.position.x = start_x
wpose.position.y = start_y
wpose.position.z = start_z
waypoints.append(copy.deepcopy(wpose))

(plan, fraction) = group.compute_cartesian_path(waypoints, 0.01, 0.0)

group.execute(plan, wait=True)
