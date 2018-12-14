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
import putitback
import putdown


class oracle():

    def __init__(self):
        rospy.init_node('oracle', anonymous=True) #initializing the 'oracle' node

    def mainfile(self):

        waypoint_1 = moveKUKA_waypoint_1.kuka()
        waypoint_2 = moveKUKA_waypoint_2.kuka()
        waypoint_3 = moveKUKA_waypoint_3.kuka()
        # pickupcup_2 = pickupcup2.arm()
        pickupcup_3 = pickupcup3.arm()
        put_it_back = putitback.arm()
        put_down = putdown.arm()


        waypoint1 = xyz_vicon.xyz_vicon('waypoint_1')
        waypoint1.talker()
        waypoint2 = xyz_vicon.xyz_vicon('waypoint_2')
        waypoint2.talker()
        waypoint3 = xyz_vicon.xyz_vicon('waypoint_3')
        waypoint3.talker()

        rospy.sleep(1)
        print "obtaining waypoints' positions"
        waypoint1xpos = waypoint1.xpos
        waypoint1ypos = waypoint1.ypos
        waypoint2xpos = waypoint2.xpos
        waypoint2ypos = waypoint2.ypos
        waypoint3xpos = waypoint3.xpos
        waypoint3ypos = waypoint3.ypos


        iteration = 0
        for iteration in range (0,10):
            print "in a for loop"
            iteration = iteration+1
            print "this is iteration # " + str(iteration)
            rospy.sleep(1)

            print "Now obtaining positions of the KUKA"
            rospy.sleep(1)


            # cup2 = xyz_vicon.xyz_vicon('cup2')
            # cup2.talker()
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
            # cup2xpos = cup2.xpos
            # cup2ypos = cup2.ypos
            cup3xpos = cup3.xpos
            cup3ypos = cup3.ypos
            kukaxpos = kuka.xpos
            kukaypos = kuka.ypos


            print "Now calculating the distances"
            rospy.sleep(1)
            distance_to_waypoint_1 = abs(sqrt((kukaxpos - waypoint1xpos)**2)+(kukaypos - waypoint1ypos)**2)
            distance_to_waypoint_2 = abs(sqrt((kukaxpos - waypoint2xpos)**2)+(kukaypos - waypoint2ypos)**2)
            distance_to_waypoint_3 = abs(sqrt((kukaxpos - waypoint3xpos)**2)+(kukaypos - waypoint3ypos)**2)

            # distance_to_cup2 = abs(sqrt((kukaxpos - cup2xpos)**2)+(kukaypos - cup2ypos)**2)
            distance_to_cup3 = abs(sqrt((kukaxpos - cup3xpos)**2)+(kukaypos - cup3ypos)**2)

            stopping_distance = 2
            pickup_distance = 0.8
            dropping_distance = 0.3
            print "Where is KUKA?"
            rospy.sleep(1)

            if distance_to_waypoint_1 < distance_to_waypoint_2 and distance_to_waypoint_1 < distance_to_waypoint_3 and distance_to_cup3 > pickup_distance:#distance_to_cup2 > pickup_distance and
                print "KUKA is next to waypoint 1 and no cup nearby"
                rospy.sleep(1)
                actions=[waypoint_3] #, waypoint_2]
                perform_action = random.choice(actions)
                if waypoint_2 == perform_action or waypoint_3 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_1 < distance_to_waypoint_2 and distance_to_waypoint_1 < distance_to_waypoint_3 and distance_to_cup3 > pickup_distance: #and distance_to_cup2 < pickup_distance
                print "KUKA is next to waypoint 1 and cup 2 nearby"
                rospy.sleep(1)
                actions=[waypoint_2, waypoint_3 ,pickupcup_2]
                perform_action = random.choice(actions)
                if waypoint_2 == perform_action or waypoint_3 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.go_to_position('cup2')
                    another_actions = [waypoint_2, waypoint_3]
                    perform_another_actions = random.choice(actions)
                    if waypoint_2 == perform_another_actions or waypoint_3 == perform_another_actions:
                        print "Now executing " + str(perform_another_actions)
                        perform_action.move_to_object()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_1 < distance_to_waypoint_2 and distance_to_waypoint_1 < distance_to_waypoint_3 and distance_to_cup3 < pickup_distance: #and distance_to_cup2 > pickup_distance:
                print "KUKA is next to waypoint 1 and cup 3 nearby"
                rospy.sleep(1)
                actions=[waypoint_2, waypoint_3, pickupcup_3]
                perform_action = random.choice(actions)
                if waypoint_2 == perform_action or waypoint_3 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.go_to_position('cup3')
                    another_actions = [waypoint_2, waypoint_3]
                    perform_another_actions = random.choice(actions)
                    if waypoint_2 == perform_another_actions or waypoint_3 == perform_another_actions:
                        print "Now executing " + str(perform_another_actions)
                        perform_another_actions.move_to_object()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_1 < distance_to_waypoint_2 and distance_to_waypoint_1 < distance_to_waypoint_3 and distance_to_cup3 > pickup_distance: #and distance_to_cup2 < dropping_distance
                print "KUKA is next to waypoint 1 and cup 2 ontop"
                rospy.sleep(1)
                actions=[waypoint_2, waypoint_3, put_it_back] #put it on top of the box
                perform_action = random.choice(actions)
                if waypoint_2 == perform_action or waypoint_3 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.main()
                    another_actions = [waypoint_2, waypoint_3]
                    perform_another_actions = random.choice(actions)
                    if waypoint_2 == perform_another_actions or waypoint_3 == perform_another_actions:
                        print "Now executing " + str(perform_another_actions)
                        perform_action.move_to_object()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_1 < distance_to_waypoint_2 and distance_to_waypoint_1 < distance_to_waypoint_3 and  distance_to_cup3 < dropping_distance:# and distance_to_cup2 > pickup_distance:
                print "KUKA is next to waypoint 1 and cup 3 ontop"
                rospy.sleep(1)
                actions=[waypoint_2, waypoint_3, put_it_back]
                perform_action = random.choice(actions)
                if waypoint_2 == perform_action or waypoint_3 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.main()
                    another_actions = [waypoint_2, waypoint_3]
                    perform_another_actions = random.choice(actions)
                    if waypoint_2 == perform_another_actions or waypoint_3 == perform_another_actions:
                        print "Now executing " + str(perform_another_actions)
                        perform_action.move_to_object()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_1 < distance_to_waypoint_2 and distance_to_waypoint_1 < distance_to_waypoint_3 and distance_to_cup3 < dropping_distance: # and distance_to_cup2 < pickup_distance:

                rospy.sleep(1)
                print "cup 3 is on top of the KUKA and cup 2 is nearby"
                actions = [waypoint_2, waypoint_3, put_it_back] #putdown cup 2
                perform_action = random.choice(actions)
                if waypoint_2 == perform_action or waypoint_3 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.go_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.main()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_1 < distance_to_waypoint_2 and distance_to_waypoint_1 < distance_to_waypoint_3 and distance_to_cup3 < pickup_distance: #and distance_to_cup2 < dropping_distance
                print "cup 2 is on top of the KUKA and cup 3 is nearby"
                actions = [waypoint_2, waypoint_3, put_it_back] #putdown cup 3
                perform_action = random.choice(actions)
                if waypoint_2 == perform_action or waypoint_3 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.go_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.main()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_2 < distance_to_waypoint_1 and distance_to_waypoint_2 < distance_to_waypoint_3 and distance_to_cup3 > pickup_distance: #and distance_to_cup2 > pickup_distance
                print "KUKA is next to waypoint 2 and no cup nearby"
                rospy.sleep(1)
                actions=[waypoint_1, waypoint_3]
                perform_action = random.choice(actions)
                if waypoint_1 == perform_action or waypoint_3 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_2 < distance_to_waypoint_1 and distance_to_waypoint_2 < distance_to_waypoint_3 and distance_to_cup3 > pickup_distance: #and distance_to_cup2 < pickup_distance
                print "KUKA is next to waypoint 2 and cup 2 nearby"
                rospy.sleep(1)
                # actions=[waypoint_1, waypoint_3, pickupcup_2]
                actions=[pickupcup_2]
                perform_action = random.choice(actions)
                if waypoint_1 == perform_action or waypoint_3 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.go_to_position('cup2')
                    another_actions = [waypoint_1, waypoint_3]
                    perform_another_actions = random.choice(actions)
                    if waypoint_1 == perform_another_actions or waypoint_3 == perform_another_actions:
                        print "Now executing " + str(perform_another_actions)
                        perform_action.move_to_object()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_2 < distance_to_waypoint_1 and distance_to_waypoint_2 < distance_to_waypoint_3 and distance_to_cup3 < pickup_distance:  #and distance_to_cup2 > pickup_distance:
                print "KUKA is next to waypoint 2 and cup 3 nearby"
                rospy.sleep(1)
                actions=[waypoint_2, waypoint_3, pickupcup_3]
                perform_action = random.choice(actions)
                if waypoint_1 == perform_action or waypoint_3 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.go_to_position('cup3')
                    another_actions = [waypoint_1, waypoint_3]
                    perform_another_actions = random.choice(actions)
                    if waypoint_1 == perform_another_actions or waypoint_3 == perform_another_actions:
                        print "Now executing " + str(perform_another_actions)
                        perform_another_actions.move_to_object()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_2 < distance_to_waypoint_1 and distance_to_waypoint_2 < distance_to_waypoint_3 and distance_to_cup3 > pickup_distance: # and distance_to_cup2 < dropping_distance :
                print "KUKA is next to waypoint 2 and cup 2 ontop"
                rospy.sleep(1)
                actions=[waypoint_1, waypoint_3, put_it_back] #put it on top of the box
                perform_action = random.choice(actions)
                if waypoint_1 == perform_action or waypoint_3 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.main()
                    another_actions = [waypoint_1, waypoint_3]
                    perform_another_actions = random.choice(actions)
                    if waypoint_1 == perform_another_actions or waypoint_3 == perform_another_actions:
                        print "Now executing " + str(perform_another_actions)
                        perform_action.move_to_object()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_2 < distance_to_waypoint_1 and distance_to_waypoint_2 < distance_to_waypoint_3  and distance_to_cup2 > pickup_distance: #and  distance_to_cup3 < dropping_distance
                print "KUKA is next to waypoint 2 and cup 3 ontop"
                rospy.sleep(1)
                actions=[waypoint_1, waypoint_3, put_it_back]
                perform_action = random.choice(actions)
                if waypoint_1 == perform_action or waypoint_3 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.main()
                    another_actions = [waypoint_1, waypoint_3]
                    perform_another_actions = random.choice(actions)
                    if waypoint_1 == perform_another_actions or waypoint_3 == perform_another_actions:
                        print "Now executing " + str(perform_another_actions)
                        perform_action.move_to_object()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_2 < distance_to_waypoint_1 and distance_to_waypoint_2 < distance_to_waypoint_3 and distance_to_cup3 < dropping_distance:  #and distance_to_cup2 < pickup_distance:

                rospy.sleep(1)
                print "cup 3 is on top of the KUKA and cup 2 is nearby"
                actions = [waypoint_1, waypoint_3, put_it_back] #putdown cup 2
                perform_action = random.choice(actions)
                if waypoint_1 == perform_action or waypoint_3 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.go_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.main()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_2 < distance_to_waypoint_1 and distance_to_waypoint_2 < distance_to_waypoint_3 and distance_to_cup3 < pickup_distance: #and distance_to_cup2 < dropping_distance
                print "cup 3 is on top of the KUKA and cup 2 is nearby"
                actions = [waypoint_1, waypoint_3, put_it_back] #putdown cup 3
                perform_action = random.choice(actions)
                if waypoint_1 == perform_action or waypoint_3 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.go_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.main()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_3 < distance_to_waypoint_2 and distance_to_waypoint_3 < distance_to_waypoint_1 and distance_to_cup3 > pickup_distance: #and distance_to_cup2 > pickup_distance
                print "KUKA is next to waypoint 3 and no cup nearby"
                rospy.sleep(1)
                actions=[waypoint_2, waypoint_1]
                perform_action = random.choice(actions)
                if waypoint_2 == perform_action or waypoint_1 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_3 < distance_to_waypoint_2 and distance_to_waypoint_3 < distance_to_waypoint_1 and distance_to_cup3 > pickup_distance: #and distance_to_cup2 < pickup_distance
                print "KUKA is next to waypoint 3 and cup 2 nearby"
                rospy.sleep(1)
                actions=[waypoint_2, waypoint_1, pickupcup_2]
                perform_action = random.choice(actions)
                if waypoint_2 == perform_action or waypoint_1 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.go_to_position('cup2')
                    another_actions = [waypoint_2, waypoint_1]
                    perform_another_actions = random.choice(actions)
                    if waypoint_2 == perform_another_actions or waypoint_1 == perform_another_actions:
                        print "Now executing " + str(perform_another_actions)
                        perform_action.move_to_object()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_3 < distance_to_waypoint_2 and distance_to_waypoint_3 < distance_to_waypoint_1 and distance_to_cup3 < pickup_distance: # and distance_to_cup2 > pickup_distance:
                print "KUKA is next to waypoint 3 and cup 3 nearby"
                rospy.sleep(1)
                actions=[waypoint_2, waypoint_1, pickupcup_3]
                perform_action = random.choice(actions)
                if pickupcup_3 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.go_to_position('cup3')
                    print "cup has been picked up"
                    another_actions = [waypoint_2, waypoint_1]
                    perform_another_actions = random.choice(another_actions)
                    if waypoint_2 == perform_another_actions or waypoint_1 == perform_another_actions:
                        print "Now executing " + str(perform_another_actions)
                        perform_another_actions.move_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()


                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_3 < distance_to_waypoint_2 and distance_to_waypoint_3 < distance_to_waypoint_1 and distance_to_cup3 > pickup_distance: #and distance_to_cup2 < dropping_distance
                print "KUKA is next to waypoint 3 and cup 2 ontop"
                rospy.sleep(1)
                actions=[waypoint_2, waypoint_1, put_it_back] #put it on top of the box
                perform_action = random.choice(actions)
                if waypoint_2 == perform_action or waypoint_1 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.main()
                    another_actions = [waypoint_2, waypoint_1]
                    perform_another_actions = random.choice(actions)
                    if waypoint_2 == perform_another_actions or waypoint_1 == perform_another_actions:
                        print "Now executing " + str(perform_another_actions)
                        perform_action.move_to_object()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_3 < distance_to_waypoint_2 and distance_to_waypoint_3 < distance_to_waypoint_1 and  distance_to_cup3 < dropping_distance: #and distance_to_cup2 > pickup_distance:
                print "KUKA is next to waypoint 3 and cup 3 ontop"
                rospy.sleep(1)
                actions=[waypoint_2, waypoint_1, put_it_back]
                perform_action = random.choice(actions)
                if waypoint_2 == perform_action or waypoint_1 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.move_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.main()
                    another_actions = [waypoint_2, waypoint_1]
                    perform_another_actions = random.choice(actions)
                    if waypoint_2 == perform_another_actions or waypoint_1 == perform_another_actions:
                        print "Now executing " + str(perform_another_actions)
                        perform_action.move_to_object()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_3 < distance_to_waypoint_2 and distance_to_waypoint_3 < distance_to_waypoint_1 and distance_to_cup3 < dropping_distance : #and distance_to_cup2 < pickup_distance:

                rospy.sleep(1)
                print "cup 3 is on top of the KUKA and cup 2 is nearby"
                actions = [waypoint_2, waypoint_1, put_it_back] #putdown cup 2
                perform_action = random.choice(actions)
                if waypoint_2 == perform_action or waypoint_1 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.go_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.main()
                rospy.sleep(1)
                print "go back to the for loop"

            if distance_to_waypoint_3 < distance_to_waypoint_2 and distance_to_waypoint_3 < distance_to_waypoint_1 and distance_to_cup3 < pickup_distance: #and distance_to_cup2 < dropping_distance
                print "cup 3 is on top of the KUKA and cup 2 is nearby"
                actions = [waypoint_2, waypoint_1, put_it_back] #putdown cup 3
                perform_action = random.choice(actions)
                if waypoint_2 == perform_action or waypoint_1 == perform_action:
                    print "Now executing " + str(perform_action)
                    perform_action.go_to_object()
                else:
                    print "Now executing " + str(perform_action)
                    perform_action.main()
                rospy.sleep(1)
                print "go back to the for loop"

if __name__ == '__main__':
    oracle = oracle() #calling kuka class
    while not rospy.is_shutdown():
        oracle.mainfile()
