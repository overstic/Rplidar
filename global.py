#!/usr/bin/env python

import numpy
import geometry_msgs.msg
import moveit_commander
import rospy
from sensor_msgs.msg import LaserScan,PointCloud2
import sys
import tf




class rplidar(object):

    def __init__(self):	
	self.ranges = []
 #   def sub(self):
	rospy.Subscriber('/scan', LaserScan, self.data)
	
 

    def data(self,a):
	angle = []
	for i in reversed(range(90)):
	    angle.append(i)
	for i in range(270,360):
	    angle.append(i)
	Range = [a.ranges[i] for i in angle]
#	rospy.loginfo_throttle(2,a.ranges[0])

	pub=rospy.Publisher('/CloudPoint',LaserScan,queue_size=10)
	msg=LaserScan()
	msg.header=a.header
	msg.header.frame_id = 'laser'
	msg.angle_min=a.angle_min
	msg.angle_max=a.angle_max
	msg.angle_increment=a.angle_increment
	msg.time_increment=a.time_increment
	msg.scan_time=a.scan_time
	msg.range_min=a.range_min
	msg.range_max=a.range_max
	List = self.ranges 
	New = numpy.hstack([List,Range])

	self.ranges = New
	if len(self.ranges) >=4500:
	    self.ranges = self.ranges[900:]
	msg.ranges=self.ranges
	msg.intensities=a.intensities
	pub.publish(msg)
	print len(msg.ranges)

#	numpy.savetxt('%d'%(i),a.ranges)
	
	#print a.ranges[0]
	




if __name__ == '__main__':
    rospy.init_node('rplidar_data', anonymous=True)
    yl = rplidar()
    rospy.spin()    	

    #rospy.spin()
    	
    


