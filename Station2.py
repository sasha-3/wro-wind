#!/usr/bin/env python3
from ev3dev.ev3 import *
import time
import math



mb = LargeMotor('outB')  
mc = LargeMotor('outC')

def upL():
    mb.position = 0
    while (mb.position) < 430:
        mb.run_direct(duty_cycle_sp = 50)
    mb.stop( stop_action = 'brake')
    mb.position = 0

def downL():
    mb.position = 0
    while mb.position > -500:
        mb.run_direct(duty_cycle_sp = -15)
    mb.stop( stop_action = 'brake')
    mb.position = 0

def Levo():
    md.position = 0
    ma.position = 0
    GO = GY.value()
    while GY.value() < (GO +  78):
        md.run_direct(duty_cycle_sp = 100)
        ma.run_direct(duty_cycle_sp = -100)
        sleep(0.05)
    md.stop( stop_action = 'brake')
    ma.stop( stop_action = 'brake')
    ma.position = 0
    md.position = 0

def upP():
    mc.position = 0
    while (mc.position) < 430:
        mc.run_direct(duty_cycle_sp = 50)
    mc.stop( stop_action = 'brake')
    mc.position = 0

def downP():
    mc.position = 0
    while mc.position > -500:
        mc.run_direct(duty_cycle_sp = -15)
    mc.stop( stop_action = 'brake')
    mc.position = 0




try:
   
    downL()

except KeyboardInterrupt:
    mb.stop( stop_action = 'brake')
    mc.stop( stop_action = 'brake')
    mb.position = 0
    mc.position = 0

