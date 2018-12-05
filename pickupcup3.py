import rospy
import sys
import arm_ik_control
import xyz_vicon
import xyz_kuka
import gripper_open
import gripper_close
import putdown
import numpy as np
from math import sqrt, cos, sin
from brics_actuator.msg import JointPositions
from brics_actuator.msg import JointValue
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from geometry_msgs.msg import TransformStamped


class arm():

    def __init__(self):
        rospy.init_node('pickupobject')
        self.arm_pub = rospy.Publisher('/arm_1/arm_controller/position_command', JointPositions, queue_size = 10)

    def go_to_position(self, object_name):
        self.object_name = object_name
        beacon1 = xyz_vicon.xyz_vicon(object_name)
        beacon1.talker()
        kuka2 = xyz_kuka.xyzkuka()
        kuka2.talker()
        rospy.sleep(2)
        xbeacon = beacon1.xpos
        ybeacon = beacon1.ypos
        zbeacon = beacon1.zpos
        print "x of cup "
        print xbeacon
        print "y of cup "
        print ybeacon
        print "z of cup "
        print zbeacon


        xkuka = kuka2.xpos
        ykuka = kuka2.ypos
        zkuka = kuka2.zpos
        theta = kuka2.yaw

        # print "x of kuka  "
        # print xkuka
        # print "y of kuka  "
        # print ykuka
        # print "z of kuka  "
        # print zkuka
        # print "yaw of kuka "
        # print theta
        #
        # print "done printing initial xyz positions"

        deltax = xbeacon - xkuka
        deltay = ybeacon - ykuka
        deltaz = (zbeacon - zkuka)

        # print "initial deltas"
        # print deltax
        # print deltay
        # print deltaz


        pos_mat = np.matrix([[deltax],[deltay]])
        rotation_angle = np.matrix([[cos(theta),sin(theta)],[-sin(theta), cos(theta)]])

        new_pos_kuka = np.dot(rotation_angle,pos_mat)
        newdeltax = new_pos_kuka[0] - 0.18
        newdeltay = new_pos_kuka[1]

        print "newdeltax"
        print newdeltax
        rospy.sleep(1)
        print "newdeltay"
        print newdeltay
        print "deltaz"
        print deltaz


        arm_ik_control.go_to_xyz(newdeltax, newdeltay, -deltaz, self.arm_pub)

if __name__ == '__main__':
    name_of_object = 'cup3'
    arm = arm()
    while not rospy.is_shutdown():
        gripper_open.main()
        arm.go_to_position(name_of_object)
        gripper_close.main()
        # rospy.sleep(3)
        # putdown.main()
