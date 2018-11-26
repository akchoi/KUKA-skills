import rospy
import sys
import arm_ik_control
import xyz_vicon
import gripper_open
import gripper_close
import pickup
import numpy as np
from brics_actuator.msg import JointPositions
from brics_actuator.msg import JointValue
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from geometry_msgs.msg import TransformStamped


class kuka():

    def __init__(self):
        rospy.init_node('pickupobject')
        self.arm_pub = rospy.Publisher('/arm_1/arm_controller/position_command', JointPositions, queue_size = 10)

    def go_to_position(self, object_name):
        self.object_name = object_name
        beacon1 = xyz_vicon.xyz_vicon(object_name)
        beacon1.talker()
        kuka2 = xyz_kuka.xyzkuka()
        kuka2.talker()
        xbeacon = beacon1.xpos
        ybeacon = beacon1.ypos
        zbeacon = beacon1.zpos
        xkuka = kuka2.xpos
        ykuka = kuka2.ypos
        zkuka = kuka2.zpos
        theta = kuka2.yaw

        pos_mat = np.matrix([xkuka],[ykuka])
        rotation_angle = np.matrix([[cos(theta),sin(theta)],[-sin(theta), cos(theta)]])

        new_pos_kuka = np.dot(rotation_angle,pos_mat)
        newkukax = new_pos_kuka[0]
        newkukay = new_pos_kuka[1]

        deltax = xbeacon - newkukax
        deltay = ybeacon - newkukay
        deltaz = zbeacon - zkuka

        arm_ik_control.go_to_xyz(deltax, deltay, deltaz, self.arm_pub)

if __name__ == '__main__':
    name_of_object = input('Name of object: ')
    kuka1 = kuka()
    while not rospy.is_shutdown():
        gripper_open.main()
        kuka1.go_to_position(name_of_object)
        gripper_close.main()
        pickup.main()
