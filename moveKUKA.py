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

    def angularvel(self,v,w): #setting the velocity to the input velocity
        newcmd = Twist()
        newcmd.linear.x = v
        newcmd.linear.y = 0
        newcmd.linear.z = 0

        newcmd.angular.x = w
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
    #
    # def move_to_object(self, object_name, stop_distance, vel_scaling_factor):
    #     """
    #     description
    #     """
    #     beacon1 = xyz_vicon.xyz_vicon("beacon1") #calling helmet class from xyz_helmet
    #     beacon1.talker() #subscribing to the xyzhelmet node
    #     kuka2 = xyz_kuka.xyzkuka() #calling xyzkuka class from xyz_kuka
    #     kuka2.talker() #subscribing to the xyzkuka node
    #     kuka1 = kuka() #calling kuka class
    #     stime = time.time()
    #     rospy.loginfo(stime)
    #     e = 0.2
    #     self.object_name =
    #
    #
    #     while (sqrt((helmet1.xpos-kuka2.xpos)**2+(helmet1.ypos-kuka2.ypos)**2) > 0.5):
    #
    #         xhelmet = helmet1.xpos
    #         yhelmet = helmet1.ypos
    #         xkuka = kuka2.xpos
    #         ykuka = kuka2.ypos
    #         d = sqrt((helmet1.xpos-kuka2.xpos)**2+(helmet1.ypos-kuka2.ypos)**2)
    #         theta = kuka2.yaw
    #
    #         # xvel = 0.1*(helmet1.xpos-kuka2.xpos)/d
    #         # yvel = 0.1*(helmet1.ypos-kuka2.ypos)/d
    #         #
    #         # vel_mat = np.array([[0.1*(helmet1.xpos-kuka2.xpos)/d],[0.1*(helmet1.ypos-kuka2.ypos)/d]])
    #         vel_mat = np.matrix([[0.1*(xhelmet - xkuka)/d],[0.1*(yhelmet-ykuka)/d]])
    #         # rotation_angle = np.array([[cos(kuka2.yaw),-sin(kuka2.yaw)],[sin(kuka2.yaw),cos(kuka2.yaw)]])
    #         rotation_angle = np.matrix([[cos(theta),sin(theta)],[-sin(theta), cos(theta)]])
    #
    #         # newvel_mat = np.dot(np.array([[cos(kuka2.yaw),-sin(kuka2.yaw)],[sin(kuka2.yaw),cos(kuka2.yaw)]]),np.array([[0.1*(helmet1.xpos-kuka2.xpos)/d],[0.1*(helmet1.ypos-kuka2.ypos)/d]]))
    #         newvel_mat = np.dot(rotation_angle,vel_mat)
    #         xvel = newvel_mat[0]
    #         yvel = newvel_mat[1]
    #
    #         constant_matrix = np.matrix([[1,0],[0,1/e]])
    #         angular_matrix = np.dot(constant_matrix,newvel_mat)
    #         vvel = angular_matrix[0]
    #         wvel = angular_matrix[1]
    #         # print "this is distance"
    #         # print(xhelmet)
    #
    #
    #         rospy.loginfo("Xvel %0.4f, Yvel %0.4f",xvel,yvel)
    #         rospy.sleep(0.5)
    #         # print "this should be the angle"
    #         # print kuka2.yaw
    #
    #         kuka1.linearvel(xvel,yvel)
    #
    #         # rospy.sleep(1) change it to 0.1 later
    #         # kuka1.linearvel((cos(kuka2.yaw)*(0.1*(helmet1.xpos-kuka2.xpos)/sqrt((helmet1.xpos-kuka2.xpos)**2\
    #         # + (helmet1.ypos-kuka2.ypos)**2))+(-sin(kuka2.yaw)*0.1*(helmet1.ypos-kuka2.ypos)/(sqrt((helmet1.xpos-kuka2.xpos)**2+(helmet1.ypos-kuka2.ypos)**2)))),
    #         # (sin(kuka2.yaw)*(0.1*(helmet1.xpos-kuka2.xpos)/(sqrt((helmet1.xpos-kuka2.xpos)**2+(helmet1.ypos-kuka2.ypos)**2)))\
    #         # +cos(kuka2.yaw)*0.1*(helmet1.ypos-kuka2.ypos)/(sqrt((helmet1.xpos-kuka2.xpos)**2+(helmet1.ypos-kuka2.ypos)**2)))) #xy plane of KUKA is different
    #
    #     kuka1.linearvel(0,0)
    #     exit()

if __name__ == '__main__':
    helmet1 = xyz_helmet.helmet() #calling helmet class from xyz_helmet
    helmet1.talker() #subscribing to the xyzhelmet node
    kuka2 = xyz_kuka.xyzkuka() #calling xyzkuka class from xyz_kuka
    kuka2.talker() #subscribing to the xyzkuka node
    kuka1 = kuka() #calling kuka class
    stime = time.time()
    rospy.loginfo(stime)
    e = 0.2
    # print "this is helmet xpos"
    # print (helmet1.xpos)
    # rospy.sleep(3)
    # print "this is helmet xpos"
    # print (helmet1.xpos)
    # print "this is kuka xpos"
    # print (kuka2.xpos)
    #
    # print (helmet1.ypos)
    # print (kuka2.ypos)
    # print((helmet1.xpos-kuka2.xpos)**2)
    # print((helmet1.ypos-kuka2.ypos)**2)
    while (sqrt((helmet1.xpos-kuka2.xpos)**2+(helmet1.ypos-kuka2.ypos)**2) > 0.5):

        xhelmet = helmet1.xpos
        yhelmet = helmet1.ypos
        xkuka = kuka2.xpos
        ykuka = kuka2.ypos
        d = sqrt((helmet1.xpos-kuka2.xpos)**2+(helmet1.ypos-kuka2.ypos)**2)
        theta = kuka2.yaw

        # xvel = 0.1*(helmet1.xpos-kuka2.xpos)/d
        # yvel = 0.1*(helmet1.ypos-kuka2.ypos)/d
        #
        # vel_mat = np.array([[0.1*(helmet1.xpos-kuka2.xpos)/d],[0.1*(helmet1.ypos-kuka2.ypos)/d]])
        vel_mat = np.matrix([[0.1*(xhelmet - xkuka)/d],[0.1*(yhelmet-ykuka)/d]])
        # rotation_angle = np.array([[cos(kuka2.yaw),-sin(kuka2.yaw)],[sin(kuka2.yaw),cos(kuka2.yaw)]])
        rotation_angle = np.matrix([[cos(theta),sin(theta)],[-sin(theta), cos(theta)]])

        # newvel_mat = np.dot(np.array([[cos(kuka2.yaw),-sin(kuka2.yaw)],[sin(kuka2.yaw),cos(kuka2.yaw)]]),np.array([[0.1*(helmet1.xpos-kuka2.xpos)/d],[0.1*(helmet1.ypos-kuka2.ypos)/d]]))
        newvel_mat = np.dot(rotation_angle,vel_mat)
        xvel = newvel_mat[0]
        yvel = newvel_mat[1]

        constant_matrix = np.matrix([[1,0],[0,1/e]])
        angular_matrix = np.dot(constant_matrix,newvel_mat)
        vvel = angular_matrix[0]
        wvel = angular_matrix[1]
        # print "this is distance"
        # print(xhelmet)
        rospy.loginfo("Xvel %0.4f, Yvel %0.4f",xvel,yvel)
        rospy.sleep(0.5)
        # print "this should be the angle"
        # print kuka2.yaw

        kuka1.linearvel(xvel,yvel)


kuka1.linearvel(0,0)
    # except rospy.ROSInterruptException:
    #     pass
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
