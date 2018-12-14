import time
import sys
import xyz_kuka
import xyz_helmet
import xyz_vicon
import numpy as np
import rospy
from math import sqrt, cos, sin
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from geometry_msgs.msg import TransformStamped


class kuka():
    #"A class for connecting to and sending commands to a kuka"

    def __init__(self):
        #rospy.init_node('Kuka_velocity', anonymous=True) #creating a node
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

    def move_to_object(self): #, object_name, stop_distance, vel_scaling_factor):
        """
        description
        """
        # self.object_name = object_name
        # self.stop_distance = stop_distance
        # self.vel_scaling_factor = vel_scaling_factor
        object_name = "waypoint_1"
        stop_distance = 0.1
        vel_scaling_factor = 0.1

        beacon1 = xyz_vicon.xyz_vicon(object_name) #calling that object class from xyz_vicon
        beacon1.talker() #subscribing to the xyzhelmet node
        kuka2 = xyz_kuka.xyzkuka() #calling xyzkuka class from xyz_kuka
        kuka2.talker() #subscribing to the xyzkuka node
        kuka1 = kuka() #calling kuka class
        stime = time.time()
        rospy.loginfo(stime)
        e = 0.2
        # print(beacon1.xpos)
        rospy.sleep(2)

        while (sqrt((beacon1.xpos-kuka2.xpos)**2+(beacon1.ypos-kuka2.ypos)**2) > stop_distance) and not rospy.is_shutdown():

            xhelmet = beacon1.xpos
            yhelmet = beacon1.ypos
            xkuka = kuka2.xpos
            ykuka = kuka2.ypos
            d = sqrt((beacon1.xpos-kuka2.xpos)**2+(beacon1.ypos-kuka2.ypos)**2)
            theta = kuka2.yaw

            vel_mat = np.matrix([[vel_scaling_factor*(xhelmet - xkuka)/d],[0.1*(yhelmet-ykuka)/d]])
            rotation_angle = np.matrix([[cos(theta),sin(theta)],[-sin(theta), cos(theta)]])

            newvel_mat = np.dot(rotation_angle,vel_mat)
            xvel = newvel_mat[0]
            yvel = newvel_mat[1]

            constant_matrix = np.matrix([[1,0],[0,1/e]])
            angular_matrix = np.dot(constant_matrix,newvel_mat)

            vvel = angular_matrix[0]
            wvel = angular_matrix[1]

            #rospy.loginfo("Xvel %0.4f, Yvel %0.4f",xvel,yvel)
            rospy.sleep(0.5)

            kuka1.linearvel(xvel,yvel)

        kuka1.linearvel(0,0)


if __name__ == '__main__':
    name_of_object = 'waypoint_1'
    stopping_distance = 0.2
    velocity_scaling_factor = 0.1
    kuka1 = kuka() #calling kuka class
    while not rospy.is_shutdown():
        kuka1.move_to_object(name_of_object,stopping_distance, velocity_scaling_factor)
