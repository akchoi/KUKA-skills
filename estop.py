import time
import sys
import numpy as np
import rospy
from math import sqrt, cos, sin
from geometry_msgs.msg import Twist


class kuka():
    #"A class for connecting to and sending commands to a kuka"

    def __init__(self):
        rospy.init_node('Kuka_emergency_stop', anonymous=True)
        self.cmd_pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)

    def stop(self):

        newcmd = Twist()
        newcmd.linear.x = 0
        newcmd.linear.y = 0
        newcmd.linear.z = 0

        newcmd.angular.x = 0
        newcmd.angular.y = 0
        newcmd.angular.z = 0

        self.cmd_pub.publish(newcmd)

if __name__ == '__main__':
    kuka1 = kuka()
    while True:
        kuka1.stop()
    rospy.spin()
