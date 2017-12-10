#!/usr/bin/env python

import roslib; roslib.load_manifest('laser_assembler')
import rospy; from laser_assembler.srv import *
from sensor_msgs.msg import PointCloud

rospy.init_node("pointcloud_assembly")
rospy.wait_for_service("assemble_scans")

pub = rospy.Publisher('assembled_cloud',PointCloud, queue_size = 10)

rate = rospy.Rate(0.2)

while not rospy.is_shutdown():
	try:
    		assemble_scans = rospy.ServiceProxy('assemble_scans', AssembleScans)
    		resp = assemble_scans(rospy.Time(0,0), rospy.get_rostime())
    		print "Got cloud with %u points" % len(resp.cloud.points)
		#msg = PointCloud()
		#msg.points = resp;
		pub.publish(resp.cloud)
		rate.sleep()
	except rospy.ServiceException, e:
    		print "Service call failed: %s"%e
