import time
import sys
import xyz_kuka
import xyz_helmet
import numpy as np
import rospy
from math import sqrt, cos, sin
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from geometry_msgs.msg import TransformStamped


class kuka():
    #"A class for connecting to and sending commands to a kuka"

    def __init__(self):
        rospy.init_node('Kuka_velocity', anonymous=True) #creating a node
        self.cmd_pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)

    def linearvel(self,x,y): #setting the velocity to the input velocity
        newcmd = Twist()
        newcmd.linear.x = x
        newcmd.linear.y = y
        newcmd.linear.z = 0

        newcmd.angular.x = 0
        newcmd.angular.y = 0
        newcmd.angular.z = 0

        self.cmd_pub.publish(newcmd)

    def stop(self): #setting the velocity to 0

        newcmd = Twist()
        newcmd.linear.x = 0
        newcmd.linear.y = 0
        newcmd.linear.z = 0

        newcmd.angular.x = 0
        newcmd.angular.y = 0
        newcmd.angular.z = 0

        self.cmd_pub.publish(newcmd)



if __name__ == '__main__':
    helmet1 = xyz_helmet.helmet() #calling helmet class from xyz_helmet
    helmet1.talker() #subscribing to the xyzhelmet node
    kuka2 = xyz_kuka.xyzkuka() #calling xyzkuka class from xyz_kuka
    kuka2.talker() #subscribing to the xyzkuka node
    kuka1 = kuka() #calling kuka class
    stime = time.time()
    rospy.loginfo(stime)
    # print (helmet1.xpos)
    # rospy.sleep(3)
    # print (helmet1.xpos)
    # print (kuka2.xpos)
    #
    # print (helmet1.ypos)
    # print (kuka2.ypos)
    # print((helmet1.xpos-kuka2.xpos)**2)
    # print((helmet1.ypos-kuka2.ypos)**2)
    d = sqrt((helmet1.xpos-kuka2.xpos)**2+(helmet1.ypos-kuka2.ypos)**2)
    while (d > 0.2):

        xhelmet = helmet1.xpos
        yhelmet = helmet1.ypos
        xkuka = kuka2.xpos
        ykuka = kuka2.ypos
        d = sqrt((helmet1.xpos-kuka2.xpos)**2+(helmet1.ypos-kuka2.ypos)**2)

        # xvel = 0.1*(helmet1.xpos-kuka2.xpos)/d
        # yvel = 0.1*(helmet1.ypos-kuka2.ypos)/d
        #
        vel_mat = np.array([[0.1*(helmet1.xpos-kuka2.xpos)/d],[0.1*(helmet1.ypos-kuka2.ypos)/d]])
        rotation_angle = np.array([[cos(kuka2.yaw),-sin(kuka2.yaw)],[sin(kuka2.yaw),cos(kuka2.yaw)]])
        newvel_mat = np.dot(np.array([[cos(kuka2.yaw),-sin(kuka2.yaw)],[sin(kuka2.yaw),cos(kuka2.yaw)]]),np.array([[0.1*(helmet1.xpos-kuka2.xpos)/d],[0.1*(helmet1.ypos-kuka2.ypos)/d]]))
        print(newvel_mat)


        # rospy.sleep(1) change it to 0.1 later
        kuka1.linearvel((cos(kuka2.yaw)*(0.1*(helmet1.xpos-kuka2.xpos)/sqrt((helmet1.xpos-kuka2.xpos)**2+(helmet1.ypos-kuka2.ypos)**2))+(-sin(kuka2.yaw)*0.1*(helmet1.ypos-kuka2.ypos)/d)),(sin(kuka2.yaw)*(0.1*(helmet1.xpos-kuka2.xpos)/d)+cos(kuka2.yaw)*0.1*(helmet1.ypos-kuka2.ypos)/d)) #xy plane of KUKA is different

    kuka1.linearvel(0,0)
    exit()
        # rospy.sleep(1)

    # while (time.time()-stime<= 5):
    #     kuka1.linearvel(0.2,0.2)
    #     # print("this is working")
    #     # rospy.sleep(1)
    # else:
    #     kuka1.linearvel(0,0.1)
    #     exit()
    #
    # rospy.spin()
