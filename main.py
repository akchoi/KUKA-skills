import rospy
import time
import sys
import numpy as np
import random
from math import sqrt, cos, sin
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

        print "this is working"

        iteration = 0
        for iteration in range (0,10):
            print "in a for loop"
            iteration = iteration+1
            print "this is iteration # " + str(iteration)
            rospy.sleep(1)

            print "Now obtaining positions of waypoints and KUKA"
            rospy.sleep(1)
            waypoint1xpos = waypoint1.xpos
            waypoint1ypos = waypoint1.ypos
            waypoint2xpos = waypoint2.xpos
            waypoint2ypos = waypoint2.ypos
            waypoint3xpos = waypoint3.xpos
            waypoint3ypos = waypoint3.ypos

            cup2 = xyz_vicon.xyz_vicon('cup2')
            cup2.talker()
            cup3 = xyz_vicon.xyz_vicon('cup3')
            cup3.talker()
            waypoint1 = xyz_vicon.xyz_vicon('waypoint_1')
            waypoint1.talker()
            waypoint2 = xyz_vicon.xyz_vicon('waypoint_2')
            waypoint2.talker()
            waypoint3 = xyz_vicon.xyz_vicon('waypoint_3')
            waypoint3.talker()

            kuka = xyz_kuka.xyzkuka()
            kuka.talker()

            rospy.sleep(1)
            cup2xpos = cup2.xpos
            cup2ypos = cup2.ypos
            cup3xpos = cup3.xpos
            cup3ypos = cup3.ypos
            kukaxpos = kuka.xpos
            kukaypos = kuka.ypos

            print "Now calculating the distances"
            rospy.sleep(1)
            distance_to_waypoint_1 = abs(sqrt((kukaxpos - waypoint1xpos)**2)+(kukaypos - waypoint1ypos)**2)
            distance_to_waypoint_2 = abs(sqrt((kukaxpos - waypoint2xpos)**2)+(kukaypos - waypoint2ypos)**2)
            distance_to_waypoint_3 = abs(sqrt((kukaxpos - waypoint3xpos)**2)+(kukaypos - waypoint3ypos)**2)

            distance_to_cup2 = abs(sqrt((kukaxpos - cup2xpos)^2)+(kukaypos - cup2ypos)^2)
            distance_to_cup3 = abs(sqrt((kukaxpos - cup3xpos)^2)+(kukaypos - cup3ypos)^2)
        # print distance_to_waypoint_1
        # print distance_to_waypoint_2
        # print distance_to_waypoint_3

            stopping_distance = 0.2
            print "Where is KUKA?"
            rospy.sleep(1)

            if distance_to_waypoint_1 <= stopping_distance and distance_to_waypoint_2 > stopping_distance and distance_to_waypoint_3 > stopping_distance and distance_to_cup2 > stopping_distance and distance_to_cup3 > stopping_distance:
                print "KUKA is next to waypoint 1 and no cup nearby"
                rospy.sleep(1)
                actions=[waypoint_2, waypoint_3]
                perform_action = random.choice(actions)
                if waypoint_2 == perform_action or waypoint_3 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_1 <= stopping_distance and distance_to_waypoint_2 > stopping_distance and distance_to_waypoint_3 > stopping_distance and distance_to_cup2 < stopping_distance and distance_to_cup3 > stopping_distance:
                print "KUKA is next to waypoint 1 and cup 2 nearby"
                rospy.sleep(1)
                actions=[waypoint_2, waypoint_3, pickupcup2]
                perform_action = random.choice(actions)
                if waypoint_2 == perform_action or waypoint_3 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.go_to_position()
                    another_actions = [waypoint_2, waypoint_3]
                    perform_another_actions = random.choice(actions)
                    if waypoint_2 == perform_another_actions or waypoint_3 == perform_another_actions:
                        print "Now executing " + str(perform_another_actions)
                        perform_action.move_to_object()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_1 <= stopping_distance and distance_to_waypoint_2 > stopping_distance and distance_to_waypoint_3 > stopping_distance and distance_to_cup3 < stopping_distance and distance_to_cup2 > stopping_distance:
                print "KUKA is next to waypoint 1 and cup 3 nearby"
                rospy.sleep(1)
                actions=[waypoint_2, waypoint_3]
                perform_action = random.choice(actions)
                if waypoint_2 == perform_action or waypoint_3 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.go_to_position()
                    another_actions = [waypoint_2, waypoint_3]
                    perform_another_actions = random.choice(actions)
                    if waypoint_2 == perform_another_actions or waypoint_3 == perform_another_actions:
                        print "Now executing " + str(perform_another_actions)
                        perform_another_actions.move_to_object()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_1 <= stopping_distance and distance_to_waypoint_2 > stopping_distance and distance_to_waypoint_3 > stopping_distance and distance_to_cup3 < stopping_distance and distance_to_cup2 < stopping_distance:
                print "KUKA is next to waypoint 1 and cup 3 and cup 2 nearby"
                rospy.sleep(1)
                if distance_to_cup2 < distance_to_cup3:
                    print "cup 2 is closer to KUKA than cup 3 is"
                    actions = [waypoint_2, waypoint_3] #putdown cup 2
                    perform_action = random.choice(actions)
                    if waypoint_2 == perform_action or waypoint_3 == perform_action:
                        print "Now executing " + str(perform_action)
                        perform_action.go_to_object()
                    else:
                        print "Now executing " + str(perform_action)
                        perform_action.main()
                if distance_to_cup2 > distance_to_cup3:
                    print "cup 3 is closer to KUKA than cup 2 is"
                    actions = [waypoint_2, waypoint_3] #putdown cup 3
                    perform_action = random.choice(actions)
                    if waypoint_2 == perform_action or waypoint_3 == perform_action:
                        print "Now executing " + str(perform_action)
                        perform_action.go_to_object()
                    else:
                        print "Now executing " + str(perform_action)
                        perform_action.main()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_1 > stopping_distance and distance_to_waypoint_2 <= stopping_distance and distance_to_waypoint_3 > stopping_distance and distance_to_cup2 > stopping_distance and distance_to_cup3 > stopping_distance:
                print "KUKA is next to waypoint 2 and no cup nearby"
                rospy.sleep(1)
                actions=[waypoint_1, waypoint_3]
                perform_action = random.choice(actions)
                if waypoint_1 == perform_action or waypoint_3 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_1 > stopping_distance and distance_to_waypoint_2 <= stopping_distance and distance_to_waypoint_3 > stopping_distance and distance_to_cup2 < stopping_distance and distance_to_cup3 > stopping_distance:
                print "KUKA is next to waypoint 2 and cup 2 nearby"
                rospy.sleep(1)
                actions=[waypoint_1, waypoint_3 , pickupcup2]
                perform_action = random.choice(actions)
                if waypoint_1 == perform_action or waypoint_3 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.go_to_position()
                    another_actions = [waypoint_1, waypoint_3]
                    perform_another_actions = random.choice(actions)
                    if waypoint_1 == perform_another_actions or waypoint_3 == perform_another_actions:
                        print "Now executing " + str(perform_another_actions)
                        perform.action.move_to_object()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_1 > stopping_distance and distance_to_waypoint_2 <= stopping_distance and distance_to_waypoint_3 > stopping_distance and distance_to_cup3 < stopping_distance and distance_to_cup2 > stopping_distance:
                print "KUKA is next to waypoint 2 and cup 3 nearby"
                rospy.sleep(1)
                actions=[waypoint_1, waypoint_3 , pickupcup3]
                perform_action = random.choice(actions)
                if waypoint_1 == perform_action or waypoint_3 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.go_to_position()
                    another_actions = [waypoint_1, waypoint_3]
                    perform_another_actions = random.choice(actions)
                    if waypoint_1 == perform_another_actions or waypoint_3 == perform_another_actions:
                        print "Now executing " + str(perform_another_actions)
                        perform.action.move_to_object()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_1 > stopping_distance and distance_to_waypoint_2 <= stopping_distance and distance_to_waypoint_3 > stopping_distance and distance_to_cup3 < stopping_distance and distance_to_cup2 < stopping_distance:
                print "KUKA is next to waypoint 2 and cup 3 and cup 2 nearby"
                rospy.sleep(1)
                if distance_to_cup2 < distance_to_cup3:
                    print "cup 2 is closer to KUKA than cup 3 is"
                    actions = [waypoint_1, waypoint_3] #putdown cup 2
                    perform_action = random.choice(actions)
                    if waypoint_1 == perform_action or waypoint_3 == perform_action:
                        print "Now executing " + str(perform_action)
                        perform_action.go_to_object()
                    else:
                        print "Now executing " + str(perform_action)
                        perform_action.main()
                if distance_to_cup2 > distance_to_cup3:
                    print "cup 3 is closer to KUKA than cup 2 is"
                    actions = [waypoint_1, waypoint_3] #putdown cup 3
                    perform_action = random.choice(actions)
                    if waypoint_1 == perform_action or waypoint_3 == perform_action:
                        print "Now executing " + str(perform_action)
                        perform_action.go_to_object()
                    else:
                        print "Now executing " + str(perform_action)
                        perform_action.main()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_1 > stopping_distance and distance_to_waypoint_2 > stopping_distance and distance_to_waypoint_3 <= stopping_distance and distance_to_cup2 > stopping_distance and distance_to_cup3 > stopping_distance:
                print "KUKA is next to waypoint 3 and no cup nearby"
                rospy.sleep(1)
                actions=[waypoint_1, waypoint_2]
                perform_action = random.choice(actions)
                if waypoint_1 == perform_action or waypoint_2 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_1 > stopping_distance and distance_to_waypoint_2 > stopping_distance and distance_to_waypoint_3 <= stopping_distance and distance_to_cup2 < stopping_distance and distance_to_cup3 > stopping_distance:
                print "KUKA is next to waypoint 3 and cup 2 nearby"
                rospy.sleep(1)
                actions=[waypoint_1, waypoint_2 , pickupcup2]
                perform_action = random.choice(actions)
                if waypoint_1 == perform_action or waypoint_2 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.go_to_position()
                    another_actions = [waypoint_1, waypoint_2]
                    perform_another_actions = random.choice(actions)
                    if waypoint_1 == perform_another_actions or waypoint_2 == perform_another_actions:
                        print "Now executing " + str(perform_another_actions)
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_1 > stopping_distance and distance_to_waypoint_2 > stopping_distance and distance_to_waypoint_3 <= stopping_distance and distance_to_cup3 < stopping_distance and distance_to_cup2 > stopping_distance:
                print "KUKA is next to waypoint 3 and cup 3 nearby"
                actions=[waypoint_1, waypoint_2]
                perform_action = random.choice(actions)
                if waypoint_1 == perform_action or waypoint_2 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.go_to_position()
                    another_actions = [waypoint_1, waypoint_2]
                    perform_another_actions = random.choice(actions)
                    if waypoint_1 == perform_another_actions or waypoint_2 == perform_another_actions:
                        print "Now executing " + str(perform_another_actions)
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_1 > stopping_distance and distance_to_waypoint_2 > stopping_distance and distance_to_waypoint_3 <= stopping_distance and distance_to_cup3 < stopping_distance and distance_to_cup2 < stopping_distance:
                print "KUKA is next to waypoint 3 and cup 3 and cup 2 nearby"
                rospy.sleep(1)
                if distance_to_cup2 < distance_to_cup3:
                    print "cup 2 is closer to KUKA than cup 3 is"
                    actions = [waypoint_1, waypoint_2] #putdown cup 2
                    perform_action = random.choice(actions)
                    if waypoint_1 == perform_action or waypoint_2 == perform_action:
                        print "Now executing " + str(perform_action)
                        perform_action.go_to_object()
                    else:
                        print "Now executing " + str(perform_action)
                        perform_action.main()
                if distance_to_cup2 > distance_to_cup3:
                    print "cup 3 is closer to KUKA than cup 2 is"
                    actions = [waypoint_1, waypoint_3] #putdown cup 3
                    perform_action = random.choice(actions)
                    if waypoint_1 == perform_action or waypoint_2 == perform_action:
                        print "Now executing " + str(perform_action)
                        perform_action.go_to_object()
                    else:
                        print "Now executing " + str(perform_action)
                        perform_action.main()
                rospy.sleep(1)
                print "go back to the for loop"

            rospy.sleep(2)

if __name__ == '__main__':
    oracle = oracle() #calling kuka class
    while not rospy.is_shutdown():
        oracle.mainfile()
