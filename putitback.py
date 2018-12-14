#!/usr/bin/env python
import rospy
import sys
from brics_actuator.msg import JointPositions
from brics_actuator.msg import JointValue
import gripper_open
import gripper_close
import time
import putdown
import arm_ik_control
import initial_position

'''
This simple script show how to publish a message to a joint. The robot will pick up a cup and place it on top of KUKA
'''
class arm():
    def __init__(self):

        # rospy.init_node('pickupobject')
        self.arm_pub = rospy.Publisher('/arm_1/arm_controller/position_command', JointPositions, queue_size = 10)

    def main(self):
        # rospy.init_node('putitback')
        arm_pub = rospy.Publisher('/arm_1/arm_controller/position_command', JointPositions, queue_size = 10)
        # arm_ik_control.go_to_xyz(0.1, -0.2, 0.3, arm_pub)


        initial_position.main()

        gripper_open.main()

        msg = JointPositions()
        rospy.sleep(5)
        print "moving joint 1" #move joint 3 and joint 2
        msg.positions = [JointValue()]
        msg.positions[0].timeStamp = rospy.Time.now()
        msg.positions[0].unit = "rad"
        msg.positions[0].joint_uri = "arm_joint_1"
        msg.positions[0].value = 0.04
        arm_pub.publish(msg)

        rospy.sleep(2)
        msg.positions[0].joint_uri = "arm_joint_5"
        msg.positions[0].value = 2.8
        arm_pub.publish(msg)
        rospy.sleep(2)

        msg.positions[0].joint_uri = "arm_joint_1"
        msg.positions[0].value = 0.01005
        arm_pub.publish(msg)

        rospy.sleep(3)
        print "moving joint 2"
        msg.positions[0].joint_uri = "arm_joint_4"
        msg.positions[0].value = 1.7
        arm_pub.publish(msg)

        rospy.sleep(2)
        msg.positions[0].joint_uri = "arm_joint_3"
        msg.positions[0].value = -0.6
        arm_pub.publish(msg)

        rospy.sleep(1)
        msg.positions[0].joint_uri = "arm_joint_2"
        msg.positions[0].value = 1.4
        arm_pub.publish(msg)




        gripper_close.main()
        rospy.sleep(2)
        initial_position.main()
        arm_ik_control.go_to_xyz_rev(-0.069, -0.447, 0.12,arm_pub)





if __name__ == "__main__":
    arm = arm()
    arm.main()
