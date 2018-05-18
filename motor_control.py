#!/usr/bin/env python

from __future__ import division
import Adafruit_PCA9685
from time import sleep


def set_servo(channel,pulse_length):
    pwm.set_pwm(channel,0,int(pulse_length*frequency*resolution/1000000))

pwm = Adafruit_PCA9685.PCA9685()

resolution = 4096

frequency = 50

channel = 0

step_speed = 4

pwm.set_pwm_freq(frequency)

Angle = [1120,1200,1280,1360,1450,1530,1610,1690,1780,1850]

while 1:
    for i,value in enumerate(Angle):
	set_servo(0,value)
	sleep(1)
    for i,value in enumerate(Angle):
	set_servo(0,Angle[-i-1])
	sleep(1)






