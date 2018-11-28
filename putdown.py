#!/usr/bin/env python
import rospy
from brics_actuator.msg import JointPositions
from brics_actuator.msg import JointValue
import gripper_open
import gripper_close
import time

'''
This simple script show how to publish a message to a joint. The robot will pick up a cup and place it on top of KUKA
'''
def main():
    pub = rospy.Publisher('/arm_1/arm_controller/position_command', JointPositions, queue_size =  10)
    #rospy.init_node('arm_test')

    '''initial positions'''

    msg = JointPositions()
    msg.positions = [JointValue()]
    msg.positions[0].timeStamp = rospy.Time.now()
    msg.positions[0].joint_uri = "arm_joint_1"
    msg.positions[0].unit = "rad"
    msg.positions[0].value = 0.011
    msg.positions[0].joint_uri = "arm_joint_2"
    msg.positions[0].unit = "rad"
    msg.positions[0].value = 0.011
    msg.positions[0].joint_uri = "arm_joint_3"
    msg.positions[0].unit = "rad"
    msg.positions[0].value = -0.016
    msg.positions[0].joint_uri = "arm_joint_4"
    msg.positions[0].unit = "rad"
    msg.positions[0].value = 0.0222
    msg.positions[0].joint_uri = "arm_joint_5"
    msg.positions[0].unit = "rad"
    msg.positions[0].value = 0.111

    pub.publish(msg)

    # time.sleep(1)
    # msg.positions[0].joint_uri = "arm_joint_1"
    # msg.positions[0].value = 1.3
    # pub.publish(msg)
    #
    # msg.positions[0].joint_uri = "arm_joint_2"
    # msg.positions[0].unit = "rad"
    # msg.positions[0].value = 1.3
    # pub.publish(msg)
    #
    # msg.positions[0].joint_uri = "arm_joint_3"
    # msg.positions[0].unit = "rad"
    # msg.positions[0].value = -1.2
    # pub.publish(msg)
    #
    # time.sleep(2)
    #
    # msg.positions[0].joint_uri = "arm_joint_4"
    # msg.positions[0].unit = "rad"
    # msg.positions[0].value = 2.8
    # pub.publish(msg)
    # gripper_open.main()
    #
    # time.sleep(2)
    #
    #
    # msg.positions[0].joint_uri = "arm_joint_2"
    # msg.positions[0].unit = "rad"
    # msg.positions[0].value = 2
    # pub.publish(msg)
    #
    # gripper_close.main()
    # time.sleep(2)
    #
    # msg.positions[0].joint_uri = "arm_joint_2"
    # msg.positions[0].unit = "rad"
    # msg.positions[0].value = 0.5
    # pub.publish(msg)
    #
    # time.sleep(2)

    msg.positions[0].joint_uri = "arm_joint_1"
    msg.positions[0].unit = "rad"
    msg.positions[0].value = 0.075
    pub.publish(msg)

    time.sleep(1)

    msg.positions[0].joint_uri = "arm_joint_2"
    msg.positions[0].unit = "rad"
    msg.positions[0].value = 1.45
    pub.publish(msg)

    time.sleep(1)

    msg.positions[0].joint_uri = "arm_joint_4"
    msg.positions[0].unit = "rad"
    msg.positions[0].value = 2.9
    pub.publish(msg)

    gripper_open.main()

    time.sleep(1)

    msg.positions[0].joint_uri = "arm_joint_2"
    msg.positions[0].unit = "rad"
    msg.positions[0].value = 0.5
    pub.publish(msg)

    rospy.spin()



if __name__ == "__main__":
    main()
