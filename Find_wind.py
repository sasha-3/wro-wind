
#!/usr/bin/env python3
from ev3dev.ev3 import *

import time, math
from time import sleep





speed = 0

ev3_1_motorA = MediumMotor('outD')  
motor_b = LargeMotor('outB')  
motor_c = LargeMotor('outC')
cl = ColorSensor('in4')
ts =  TouchSensor('in3')
gy = GyroSensor('in2')




#Функция для движения робота-поисковика
def Prav():
    motor_b.position = 0
    motor_c.position = 0
    while (motor_b.position) < 500:
        motor_b.run_direct(duty_cycle_sp = 80)
        motor_c.run_direct(duty_cycle_sp = -80)
    motor_b.stop( stop_action = 'brake')
    motor_c.stop( stop_action = 'brake')
    motor_b.position = 0
    motor_c.position = 0

def Pramo():
    motor_b.position = 0
    motor_c.position = 0
    motor_b.run_direct(duty_cycle_sp = 80)
    motor_c.run_direct(duty_cycle_sp = -80)
    sleep(100)

def Levo():
    motor_b.position = 0
    motor_c.position = 0
    go = gy.value()
    while gy.value() < (go +  78):
        motor_b.run_direct(duty_cycle_sp = -100)
        motor_c.run_direct(duty_cycle_sp = 100)
        sleep(0.05)
    motor_b.stop( stop_action = 'brake')
    motor_c.stop( stop_action = 'brake')
    motor_c.position = 0
    motor_b.position = 0
    


def Forward():
    motor_b.position = 0
    motor_c.position = 0
    while (motor_b.position) < 1100:
        motor_b.run_direct(duty_cycle_sp = 80)
        motor_c.run_direct(duty_cycle_sp = 80)
    motor_b.stop( stop_action = 'brake')
    motor_c.stop( stop_action = 'brake')
    
def Back():
    motor_b.position = 0
    motor_c.position = 0
    while (motor_b.position) > -600:
        motor_b.run_direct(duty_cycle_sp = -80)
        motor_c.run_direct(duty_cycle_sp = -80)
    motor_b.stop( stop_action = 'brake')
    motor_c.stop( stop_action = 'brake')
    motor_b.position = 0
    motor_c.position = 0





def speed_counter_fast():
    global speed
    cl.mode = 'COL-REFLECT'
    prevClr = False
    spinTime = time.time()
    counter = 0
    while True:
        if (cl.value() > 20) != prevClr:
            prevClr = not prevClr
            speed = time.time() - spinTime
            spinTime = time.time()
            counter += 1
            if counter >= 10:
                print(speed)
                counter = 0

#Функции для робота-установщик


# грамма




# print('Press Button')
# while(ts.is_pressed == False):
#     print('Press Button')
#     sleep(00.1)
if __name__ == '__main__':
    try:

        motor_b.run_direct(duty_cycle_sp = 100)
        motor_c.run_direct(duty_cycle_sp = -100)
        sleep(100)

    
    except KeyboardInterrupt:
        mWind.stop( stop_action = 'brake')
        motor_b.stop( stop_action = 'brake')
        motor_c.stop( stop_action = 'brake')
        motor_b.reset()
        motor_c.reset()   
        mWind.reset()
    



# def speed_counter():
#     global speed
#     cl.mode = 'COL-REFLECT'
#     new_color, old_color = 1, 1
#     count, rotation = 0, 0
#     start_time_of_rotation = 0
#     end_time_of_rotation = 0
