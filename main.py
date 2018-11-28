import rospy
import time
import sys
import numpy as np
import random
import math
import moveKUKA_waypoint_1
import moveKUKA_waypoint_2
import moveKUKA_waypoint_3
import pickupcup2
import pickupcup3
import xyz_kuka
import xyz_vicon


class oracle():

    def __init__(self):
        rospy.init_node('oracle', anonymous=True) #initializing the 'oracle' node

    def mainfile(self):

        waypoint_1 = moveKUKA_waypoint_1.kuka()
        waypoint_2 = moveKUKA_waypoint_2.kuka()
        waypoint_3 = moveKUKA_waypoint_3.kuka()

        # cup2 = xyz_vicon.xyz_vicon('cup2')
        # cup2xpos = cup2.xpos
        # cup2ypos = cup2.ypos
        # cup3 = xyz_vicon.xyz_vicon('cup3')
        # cup3xpos = cup3.xpos
        # cup3ypos = cup3.ypos

        waypoint1 = xyz_vicon.xyz_vicon('waypoint_1')
        waypoint1.talker()
        waypoint2 = xyz_vicon.xyz_vicon('waypoint_2')
        waypoint2.talker()
        waypoint3 = xyz_vicon.xyz_vicon('waypoint_3')
        waypoint3.talker()

        kuka = xyz_kuka.xyzkuka()
        kuka.talker()

        rospy.sleep(2)

        waypoint1xpos = waypoint1.xpos
        waypoint2xpos = waypoint2.xpos
        waypoint3xpos = waypoint3.xpos

        kukaxpos = kuka.xpos
        kukaypos = kuka.ypos

        # distance_to_cup2 = abs(sqrt((kukaxpos - cup2xpos)^2)+(kukaypos - cup2ypos)^2)
        # distance_to_cup3 = abs(sqrt((kukaxpos - cup3xpos)^2)+(kukaypos - cup3ypos)^2)

        distance_to_waypoint_1 = abs(kukaxpos - waypoint1xpos)
        distance_to_waypoint_2 = abs(kukaxpos - waypoint2xpos)
        distance_to_waypoint_3 = abs(kukaxpos - waypoint3xpos)

        value = 0.5

        timeout = time.time() + 60*5 # 5 minutes from now
        while True:
            if distance_to_waypoint_1 <= value and distance_to_waypoint_2 > value and distance_to_waypoint_3 > value: #distance_to_cup2 < value and distance_to_cup3 > value:
                print "KUKA is next to waypoint 1"
                actions=[waypoint_2, waypoint_3] #, pickupcup2]
                perform_action = random.choice(actions)
                if waypoint_2 == perform_action or waypoint_3 == perform_action:
                    print "Now executing" + perform_action
                    perform_action.move_to_object()
            rospy.sleep(2)
            elif distance_to_waypoint_1 > value and distance_to_waypoint_2 <= value and distance_to_waypoint_3 > value: #distance_to_cup2 > value and distance_to_cup3 < value:
                print "KUKA is next to waypoint 2"
                actions=[waypoint_1, waypoint_3] #, pickupcup3]
                perform_action = random.choice(actions)
                if waypoint_1 == perform_action or waypoint_3 == perform_action:
                    print "Now executing" + perform_action
                    perform_action.move_to_object()
            rospy.sleep(2)
            elif distance_to_waypoint_1 > value and distance_to_waypoint_2 > value and distance_to_waypoint_3 <= value:
                print "KUKA is next to waypoint 3"
                actions=[waypoint_1, waypoint_2]
                perform_action = random.choice(actions)
                if waypoint_1 == perform_action or waypoint_2 == perform_action:
                    print "Now executing" + perform_action
                    perform_action.move_to_object()
            rospy.sleep(2)
            elif time.time() > timeout:
                break

if __name__ == '__main__':
    oracle = oracle() #calling kuka class
    while not rospy.is_shutdown():
        oracle.mainfile()
