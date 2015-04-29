#!/usr/bin/env python

import sys
import rospy
import roslib
import RPi.GPIO as GPIO
import time

from std_msgs.msg import Int64
#from ultracom.msg import ultrasensor
#to use msg -> excute.. catkin_make -> fuck

#when trig pin = 20, echo pin 21

trig_pin=20
echo_pin=21

def talker():

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trig_pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(echo_pin, GPIO.IN)

    pub=rospy.Publisher("distance",Int64, queue_size=10)
    rospy.init_node("ultranode", anonymous=True)
    rate=rospy.Rate(1)

    while not rospy.is_shutdown():
	  GPIO.output(trig_pin, True)
	  time.sleep(0.00001)
	  GPIO.output(trig_pin, False)
	  start = time.time()
	  while GPIO.input(echo_pin)==0:
	     start=time.time()
          while GPIO.input(echo_pin)==1:
	     stop = time.time()

	  elapsed = stop-start
	  distance = elapsed * 34000/2
	  pub.publish(distance)
          rate.sleep()


if __name__ == "__main__":
   try:
	talker()
   except rospy.ROSInterruptException:
	pass
	
