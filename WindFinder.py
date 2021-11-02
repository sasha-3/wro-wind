
from ev3dev.ev3 import *
import ev3dev.ev3
import time
from time import sleep
from threading import Thread
import sys 
import math 

#Установщик
mWind = MediumMotor('outD')  
mb_1 = LargeMotor('outB')  
mc_1 = LargeMotor('outC')  
ma_1 = LargeMotor('outA')
cl = ColorSensor('in4')
ts = TouchSensor('in3')
gy = GyroSensor('in2')

speed = 0 
speedr = 0
#Функция для движения робота-поисковика
def Prav():
    mb_1.position = 0
    mc_1.position = 0
    go = gy.value()
    
    while gy.value() > (go -  88):
        mb_1.run_direct(duty_cycle_sp = -30)
        mc_1.run_direct(duty_cycle_sp = 30)
        print(gy.value())
        sleep(0.005)
    mb_1.stop( stop_action = 'brake')
    mc_1.stop( stop_action = 'brake')
    mc_1.position = 0
    mb_1.position = 0
    
#Функция для движения робота-поисковика
def Levo():
    
    mb_1.position = 0
    mc_1.position = 0
    go = gy.value()
    
    while gy.value() < (go +  88):
        mb_1.run_direct(duty_cycle_sp = 30)
        mc_1.run_direct(duty_cycle_sp = -30)
        print(gy.value())
        sleep(0.005)
    mb_1.stop( stop_action = 'brake')
    mc_1.stop( stop_action = 'brake')
    mc_1.position = 0
    mb_1.position = 0
    
#Функция для движения робота-поисковика


    
#Функция для движения робота-поисковика
def Back():
    mb_1.position = 0
    mc_1.position = 0
    while (mb_1.position) > -600:
        mb_1.run_direct(duty_cycle_sp = -80)
        mc_1.run_direct(duty_cycle_sp = -80)
    mb_1.stop( stop_action = 'brake')
    mc_1.stop( stop_action = 'brake')
    mb_1.position = 0
    mc_1.position = 0



# СЧЕТЧИК ОБОРОТОВ 
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
            if counter >= 2:
                speedr = round(speed, 2)
                print(speedr)
                counter = 0

def Forward():
    mb_1.position = 0
    mc_1.position = 0
    while (mb_1.position) < 1800:
        mb_1.run_direct(duty_cycle_sp = 30)
        mc_1.run_direct(duty_cycle_sp = 30)
        if(speed) < 0.07:
            mb_1.stop( stop_action = 'brake')
            mc_1.stop( stop_action = 'brake')
            print('<  0.7')
    mb_1.stop( stop_action = 'brake')
    mc_1.stop( stop_action = 'brake')

if __name__ == "__main__":
    try:
        while(ts.is_pressed == False):
            print('Press Button')
            sleep(0.1)    

        print("start")
        speed_counter_Thread = Thread(target=speed_counter_fast)
        speed_counter_Thread.start()
        
        mb_1.position, mc_1.position = 0, 0


        length = 3550
        max_speed = 0
        while (mb_1.position < length) and (mc_1.position < length):
            mb_1.run_direct(duty_cycle_sp = 80)
            mc_1.run_direct(duty_cycle_sp = 80)
            if speed > max_speed:
                max_speed = speed
                max_speed_enc_b = mb_1.position
                max_speed_enc_c = mc_1.position

        print(max_speed_enc_b,max_speed_enc_c,max_speed)

        while (mb_1.position > max_speed_enc_b) and (mc_1.position > max_speed_enc_c):
            mb_1.run_direct(duty_cycle_sp = -80)
            mc_1.run_direct(duty_cycle_sp = -80)
        # b_x, c_x = mb_1.position, mc_1.position

        print("------------")
        # print(b_x,c_x)
        mb_1.stop( stop_action = 'brake')
        mc_1.stop( stop_action = 'brake')
        mb_1.position = 0
        mc_1.position = 0
        
        sleep(0.5)
        Levo()
        sleep(0.5)
        
        mWind.position = 0
        while (mWind.position) > -90:
            mWind.run_direct(duty_cycle_sp = -40)
        mWind.stop( stop_action = 'brake')
        mWind.position = 0
        

        Forward()

        ma_1.position = 0
        while (ma_1.position) < 170:
            ma_1.run_direct(duty_cycle_sp = 20)
        ma_1.stop( stop_action = 'brake')
        ma_1.position = 0
        sleep(2)
                
        
        sleep(0.5)
        # Мы доехали в конечную точку, тут надо поднять цветную метку
        Levo()

        mb_1.position = 0
        mc_1.position = 0
        while  (max_speed_enc_b) > (mb_1.position):
            mb_1.run_direct(duty_cycle_sp = 80)
            mc_1.run_direct(duty_cycle_sp = 80)
        mb_1.stop( stop_action = 'brake')
        mc_1.stop( stop_action = 'brake')
        mb_1.position = 0
        mc_1.position = 0

        mb_1.position = 0
        mc_1.position = 0
        while  (250) > (mb_1.position):
            mb_1.run_direct(duty_cycle_sp = 80)
            mc_1.run_direct(duty_cycle_sp = 80)
        mb_1.stop( stop_action = 'brake')
        mc_1.stop( stop_action = 'brake')
        mb_1.position = 0
        mc_1.position = 0

    except Exception:
        mb_1.stop()
        mc_1.stop()
        mb_1.reset()
        mc_1.reset()
        sys.exit(0)