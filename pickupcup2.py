import rospy
import sys
import arm_ik_control
import xyz_vicon
import xyz_kuka
import gripper_open
import gripper_close
import putdown
import numpy as np
import initial_position
from math import sqrt, cos, sin
from brics_actuator.msg import JointPositions
from brics_actuator.msg import JointValue
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from geometry_msgs.msg import TransformStamped


class arm():

    def __init__(self):
        # rospy.init_node('pickupobject')
        self.arm_pub = rospy.Publisher('/arm_1/arm_controller/position_command', JointPositions, queue_size = 10)

    def go_to_position(self, object_name):
        initial_position.main()
        self.object_name = 'cup2'
        beacon1 = xyz_vicon.xyz_vicon('cup2')
        beacon1.talker()
        kuka2 = xyz_kuka.xyzkuka()
        kuka2.talker()
        rospy.sleep(1)
        put_down = putdown.arm()
        xbeacon = beacon1.xpos
        ybeacon = beacon1.ypos
        zbeacon = beacon1.zpos

        xkuka = kuka2.xpos
        ykuka = kuka2.ypos
        zkuka = kuka2.zpos
        theta = kuka2.yaw

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


        print "printing newdeltay"
        print newdeltay
        print "printing newdeltax"
        print newdeltax - 0.02
        print "printing deltaz"
        print -deltaz + 0.1

        rospy.sleep(1)
        print "now working"

        arm_ik_control.go_to_xyz(newdeltax - 0.02 , newdeltay + 0.12, -deltaz + 0.1, self.arm_pub)
        rospy.sleep(5)
        print "now about to grab the cup"
        arm_ik_control.go_to_xyz(newdeltax - 0.02 , newdeltay + 0.04, -deltaz + 0.1, self.arm_pub)
        rospy.sleep(2)
        gripper_close.main()
        rospy.sleep(2)
        put_down.main()
        rospy.sleep(2)
        initial_position.main()

    def drop_off(self, object_name):
        # self.object_name = object_name
        # beacon1 = xyz_vicon.xyz_vicon(object_name)

        rospy.sleep(1)
        print "now working"

        gripper_open.main()
        gripper_close.main()
        rospy.sleep(3)
        arm_ik_control.go_to_xyz_rev(0.2 ,-0.4, 0.1, self.arm_pub)
        gripper_open.main()
        gripper_close.main()
        rospy.sleep(3)
        put_down.main()
        initial_position.main()



if __name__ == '__main__':

    name_of_object = 'cup2'
    arm = arm()
    gripper_open.main()
    rospy.sleep(1)
    arm.go_to_position(name_of_object)

    # arm.drop_off(name_of_object)


    # rospy.sleep(3)
    # putdown.main()
