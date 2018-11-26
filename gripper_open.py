#!/usr/bin/env python
import rospy
from brics_actuator.msg import JointPositions
from brics_actuator.msg import JointValue
from brics_actuator.msg import Poison

import time

'''
This simple script show how to publish a message to a joint. The robot will wave hello to you when running this script
'''
def main(): 
    pub = rospy.Publisher('/arm_1/gripper_controller/position_command', JointPositions, queue_size =  10)
    #rospy.init_node('gripper_test')

    msg = JointPositions()
    msg.positions = [JointValue()]
    msg.positions[0].timeStamp = rospy.Time.now()
    msg.positions[0].joint_uri = "gripper_finger_joint_l"
    msg.positions[0].unit = "m"
    msg.positions[0].value = 0.0
    pub.publish(msg)

    msg.positions[0].joint_uri = "gripper_finger_joint_r"
    msg.positions[0].unit = "m"
    msg.positions[0].value = 0.0
    pub.publish(msg)


    time.sleep(1)
    msg.positions[0].joint_uri = "gripper_finger_joint_l"
    msg.positions[0].unit = "m"
    msg.positions[0].value = 0.0114
    pub.publish(msg)

    time.sleep(1)
    pub.publish(msg)

    msg.positions[0].joint_uri = "gripper_finger_joint_r"
    msg.positions[0].unit = "m"
    msg.positions[0].value = 0.0114
    pub.publish(msg)

    def file_exit():
      print "shutting down"

    rospy.on_shutdown(file_exit)
if __name__ == "__main__":
    main()
