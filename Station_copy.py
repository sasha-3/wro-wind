#!/usr/bin/env python3
from ev3dev.ev3 import *
import time
import math
from time import sleep

x , y = 0,0


mb = LargeMotor('outB')# 
mc = LargeMotor('outC')#
md = LargeMotor('outD')  
ma = LargeMotor('outA')
Gyro = GyroSensor('in1')
Sony1 = UltrasonicSensor('in2')
T = TouchSensor('in3')
#Sony2 = UltrasonicSensor('in3')
#Sony3 = UltrasonicSensor('in4')

def upL():
    mb.position = 0
    while (mb.position) < 430:
        mb.run_direct(duty_cycle_sp = 50)
    mb.stop( stop_action = 'brake')
    mb.position = 0

def downL():
    mb.position = 0
    while mb.position > -475:
        mb.run_direct(duty_cycle_sp = -17)
        
    mb.stop( stop_action = 'brake')
    mb.position = 0





def UpP():
    mc.run_direct(duty_cycle_sp = 30)
    sleep(6)
    mc.stop( stop_action = 'brake')

def downP():
    mc.run_direct(duty_cycle_sp = -30)
    sleep(6)
    mc.stop( stop_action = 'brake')


def X(x):
    md.position = 0
    ma.position = 0
    while (md.position) < x*0.86:
        ma.run_direct(duty_cycle_sp = 100)
        md.run_direct(duty_cycle_sp = 100)
    ma.stop( stop_action = 'brake')
    md.stop( stop_action = 'brake')
    md.position = 0
    ma.position = 0


def Y(y):
    md.position = 0
    ma.position = 0
    while (md.position) < y*0.86:
        ma.run_direct(duty_cycle_sp = 100)
        md.run_direct(duty_cycle_sp = 100)
    ma.stop( stop_action = 'brake')
    md.stop( stop_action = 'brake')
    md.position = 0
    ma.position = 0

def Levo():
    md.position = 0
    ma.position = 0
    GO = Gyro.value()
    while Gyro.value() > (GO -  88):
        md.run_direct(duty_cycle_sp = 100)
        ma.run_direct(duty_cycle_sp = -100)
        sleep(0.05)
    md.stop( stop_action = 'brake')
    ma.stop( stop_action = 'brake')
    ma.position = 0
    md.position = 0
    

def Prav():
    md.position = 0
    ma.position = 0
    while (md.position) < 2400:
        ma.run_direct(duty_cycle_sp = -100)
        md.run_direct(duty_cycle_sp = 100)
    ma.stop( stop_action = 'brake')
    md.stop( stop_action = 'brake')
    md.position = 0
    ma.position = 0
      


def Back():
    md.position = 0
    ma.position = 0
    while md.position > -2100:
        ma.run_direct(duty_cycle_sp = -100)
        md.run_direct(duty_cycle_sp = -100)
    ma.stop( stop_action = 'brake')
    md.stop( stop_action = 'brake')
    md.position = 0
    ma.position = 0
   


def Razvorot():
    md.position = 0
    ma.position = 0
    while (md.position) < 5000:
        ma.run_direct(duty_cycle_sp = -100)
        md.run_direct(duty_cycle_sp = 100)
    ma.stop( stop_action = 'brake')
    md.stop( stop_action = 'brake')
    md.position = 0
    ma.position = 0
      



try:

    downP()
    UpP()










except KeyboardInterrupt:
    mb.stop( stop_action = 'brake')
    mc.stop( stop_action = 'brake')
    ma.stop( stop_action = 'brake')
    md.stop( stop_action = 'brake')
    mb.position = 0
    mc.position = 0
    md.position = 0   
    ma.position = 0





