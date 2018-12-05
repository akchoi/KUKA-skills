#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import TransformStamped
import tf
from geometry_msgs.msg import Quaternion
from math import *


#pub = rospy.Publisher('tag_detections', std_msgs.msg.String, queue_size = 10)

class xyzkuka():

    def __init__(self):
        self.xyzpos = []
        self.xpos = []
        self.ypos = []
        self.zpos = []

    def callback_kuka(self,data):
        #rospy.loginfo(data.detections) #need to find the format
        #xyz =data.pos6584198
        if data.transform:
            self.xyzpos = data.transform.translation
            self.xpos = data.transform.translation.x
            self.ypos = data.transform.translation.y
            self.zpos = data.transform.translation.z

            self.xrotq = data.transform.rotation.x
            self.yrotq = data.transform.rotation.y
            self.zrotq = data.transform.rotation.z
            self.wrotq = data.transform.rotation.w

            self.quaternion = (self.xrotq,self.yrotq,self.zrotq,self.wrotq)
            self.euler = tf.transformations.euler_from_quaternion(self.quaternion)
            self.roll = self.euler[0]
            self.pitch = self.euler[1]
            self.yaw = self.euler[2]

            # print("x: {} y: {}".format(self.xpos, self.ypos))



    def talker(self):
        #rospy.init_node('xyz_kuka', anonymous=True) #names the node
        #rate = rospy.Rate(0.1) # 10hz
        rospy.Subscriber("vicon/kuka/kuka", TransformStamped, self.callback_kuka) #where the information is coming from, type, information
        #rospy.spin() #simply keeps python from exiting until this node is stopped


if __name__ == '__main__':
    rospy.init_node('xyz_kuka', anonymous=True) #names the node
    try:
        xyzkuka1 = xyzkuka()
        xyzkuka1.talker()
    except rospy.ROSInterruptException:
        pass

    rospy.spin()


#pub = rospy.Publisher('andystalker', AprilTagDetectionArray, queue_size=10)
#pub.Publisher(xyZ)
