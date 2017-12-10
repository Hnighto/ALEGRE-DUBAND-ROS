#!/usr/bin/env python

import rospy 
from std_msgs.msg import Float64



rospy.init_node('rotvel') #declare la creation d'un noeud : ne doit etre appelee qu'une fois par noeud

pub = rospy.Publisher('output', Float64, queue_size = 10)

rate = rospy.Rate(10); #limite la frequence d'une boucle a 10 HZ

while not rospy.is_shutdown():
	msg = Float64()
	msg.data = 1.0
	pub.publish(msg)
	rate.sleep()

