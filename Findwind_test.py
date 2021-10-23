#!/usr/bin/env python3
from ev3dev.ev3 import *
import time
import math
from time import sleep


mWind = MediumMotor('outD')  
mb = LargeMotor('outB')  
mc = LargeMotor('outC')
cl = ColorSensor('in4')
gy = GyroSensor('in2')


gy.mode = 'GYRO-ANG'


def Prav():
    mb.position = 0
    mc.position = 0
    go = gy.value()
    while gy.value() < (90 + go):
        mb.run_direct(duty_cycle_sp = -100)
        mc.run_direct(duty_cycle_sp = 100)
        sleep(0.05)
    mb.stop( stop_action = 'brake')
    mc.stop( stop_action = 'brake')
    mb.position = 0
    mc.position = 0


def Levo():
    mb.position = 0
    mc.position = 0
    go = gy.value()
    while gy.value() > (go - 360):
        mb.run_direct(duty_cycle_sp = 100)
        mc.run_direct(duty_cycle_sp = -100)
        sleep(0.05)
    mb.stop( stop_action = 'brake')
    mc.stop( stop_action = 'brake')
    mb.position = 0
    mc.position = 0

def Forward():
    mb.position = 0
    mc.position = 0


def Back():
    mb.position = 0
    mc.position = 0
    while (mb.position) < -600:
        mb.run_direct(duty_cycle_sp = -80)
        mc.run_direct(duty_cycle_sp = -80)
    mb.stop( stop_action = 'brake')
    mc.stop( stop_action = 'brake')
    mb.position = 0
    mc.position = 0

Levo()    
sleep(1)
mWind.position = 0
while mWind.position > -80:
    mWind.run_direct(duty_cycle_sp = -50)
mWind.stop(stop_action = 'brake')

    


# cl.mode = 'COL-REFLECT'
# new_color, old_color = 1, 1
# count, rotation = 0, 0
# start_time_of_rotation = 0
# end_time_of_rotation = 0
# #R = 3.5 sm
# circle_lenght = math.pi * 2 * 3.5 * 0.01
# start_time_of_rotation = time.time()
# while True:
#     old_color = new_color
#     if cl.value() > 20:
#         new_color = 1
#     else:
#         new_color = 0

#     if (new_color + old_color) == 1:
#         count += 1

#     if count == 8:
#         end_time_of_rotation = time.time()
#         speed  = circle_lenght / (end_time_of_rotation - start_time_of_rotation)
#         rotation += 1
#         print(rotation, speed)
#         count = 0
#         start_time_of_rotation = time.time()
#     time.sleep(0.001)
#     mb.run_direct(duty_cycle_sp = 80)
#     mc.run_direct(duty_cycle_sp = 80)s

    
#  ##   if( speed > 2 ):
# ##        mb.run_direct(duty_cycle_sp = 0)
#  ###       mc.run_direct(duty_cycle_sp = 0)
#  ##   else:
#  ###       mb.run_direct(duty_cycle_sp = 80)
#  ##       mc.run_direct(duty_cycle_sp = 80)
















# #     mb.run_direct(duty_cycle_sp = 50)
#  #   mc.run_direct(duty_cycle_sp = 50)
#   #  if 