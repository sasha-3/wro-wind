#!/usr/bin/env python3
from ev3dev.ev3 import *
import time
import math



# mb = LargeMotor('outB')  
# mc = LargeMotor('outC')
md = LargeMotor('outD')  
ma = LargeMotor('outA')
# mb.position = 0
# mc.position = 0
md.position = 0
ma.position = 0
try:
     while (mb.position) < -600:
        ma.run_direct(duty_cycle_sp = -80)
        md.run_direct(duty_cycle_sp = -80)
    ma.stop( stop_action = 'brake')
    md.stop( stop_action = 'brake')
    ma.position = 0
    md.position = 0

except KeyboardInterrupt:
    # mb.stop( stop_action = 'brake')
    # mc.stop( stop_action = 'brake')
    ma.stop( stop_action = 'brake')
    md.stop( stop_action = 'brake')
    # mb.position = 0
    # mc.position = 0
    md.position = 0
    ma.position = 0














































