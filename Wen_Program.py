
#!/usr/bin/env python3
# from Station import Razvorot

from threading import Thread
import time, math, os, sys, rpyc
from time import sleep

import rpyc

ev3_host_1 = "192.168.43.83"
ev3_host_2 = "192.168.43.238"
ev3_host_3 = "192.168.43.126"

ev3_connection_1 = rpyc.classic.connect(ev3_host_1)
ev3_connection_2 = rpyc.classic.connect(ev3_host_2)
ev3_connection_3 = rpyc.classic.connect(ev3_host_3)


ev3dev2_motor_1 = ev3_connection_1.modules['ev3dev2.motor']
ev3dev2_motor_2 = ev3_connection_2.modules['ev3dev2.motor']
ev3dev2_motor_3 = ev3_connection_3.modules['ev3dev2.motor']

ev3dev2_sensor_1 = ev3_connection_1.modules['ev3dev2.sensor']
ev3dev2_sensor_2 = ev3_connection_2.modules['ev3dev2.sensor']
ev3dev2_sensor_3 = ev3_connection_3.modules['ev3dev2.sensor']


ev3dev2_sensor_lego_1 = ev3_connection_1.modules['ev3dev2.sensor.lego']
ev3dev2_sensor_lego_2 = ev3_connection_2.modules['ev3dev2.sensor.lego']
ev3dev2_sensor_lego_3 = ev3_connection_3.modules['ev3dev2.sensor.lego']



# mWind = MediumMotor('outD')  
# mb_1 = LargeMotor('outB')  
# mc_1 = LargeMotor('outC')
# cl = ColorSensor('in4')
# ts =  TouchSensor('in3')
# gy = GyroSensor('in2')

#Установщик
mWind = ev3dev2_motor_1.MediumMotor(ev3dev2_motor_1.OUTPUT_D)  
mb_1 = ev3dev2_motor_1.LargeMotor(ev3dev2_motor_1.OUTPUT_B)  
mc_1 = ev3dev2_motor_1.LargeMotor(ev3dev2_motor_1.OUTPUT_C)  
cl = ev3dev2_sensor_lego_1.ColorSensor(ev3dev2_sensor_1.INPUT_4)
ts =  ev3dev2_sensor_lego_1.TouchSensor(ev3dev2_sensor_1.INPUT_3)
gy = ev3dev2_sensor_lego_1.GyroSensor(ev3dev2_sensor_1.INPUT_2)

#Установщик движение 
ma_2 = ev3dev2_motor_2.LargeMotor(ev3dev2_motor_2.OUTPUT_A)
mb_2 = ev3dev2_motor_2.LargeMotor(ev3dev2_motor_2.OUTPUT_B)  
mc_2 = ev3dev2_motor_2.LargeMotor(ev3dev2_motor_2.OUTPUT_C)
md_2 = ev3dev2_motor_2.LargeMotor(ev3dev2_motor_2.OUTPUT_D)  

GY = ev3dev2_sensor_lego_2.GyroSensor(ev3dev2_sensor_2.INPUT_1)
T = ev3dev2_sensor_lego_2.TouchSensor(ev3dev2_sensor_2.INPUT_3)
Sony1 = ev3dev2_sensor_lego_2.UltrasonicSensor(ev3dev2_sensor_2.INPUT_2)
#установщик подемники
ma_3 = ev3dev2_motor_3.LargeMotor(ev3dev2_motor_3.OUTPUT_A)
mb_3 = ev3dev2_motor_3.LargeMotor(ev3dev2_motor_3.OUTPUT_B)  
mc_3 = ev3dev2_motor_3.LargeMotor(ev3dev2_motor_3.OUTPUT_C)
md_3 = ev3dev2_motor_3.LargeMotor(ev3dev2_motor_3.OUTPUT_D)  


GY.mode='GYRO-ANG'







speed = 0






#Функция для движения робота-поисковика
def Prav():
    mb_1.position = 0
    mc_1.position = 0
    while (mb_1.position) < 500:
        mb_1.run_direct(duty_cycle_sp = 80)
        mc_1.run_direct(duty_cycle_sp = -80)
    mb_1.stop( stop_action = 'brake')
    mc_1.stop( stop_action = 'brake')
    mb_1.position = 0
    mc_1.position = 0

def Levo():
    mb_1.position = 0
    mc_1.position = 0
    go = gy.value()
    while gy.value() < (go +  75):
        mb_1.run_direct(duty_cycle_sp = -100)
        mc_1.run_direct(duty_cycle_sp = 100)
        sleep(0.05)
    mb_1.stop( stop_action = 'brake')
    mc_1.stop( stop_action = 'brake')
    mc_1.position = 0
    mb_1.position = 0
    


def Forward():
    mb_1.position = 0
    mc_1.position = 0
    while (mb_1.position) < 1100:
        mb_1.run_direct(duty_cycle_sp = 80)
        mc_1.run_direct(duty_cycle_sp = 80)
    mb_1.stop( stop_action = 'brake')
    mc_1.stop( stop_action = 'brake')
    
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
def upL():
    mb_3.position = 0
    md_3.position = 0
    mb_3.run_direct(duty_cycle_sp = 50)
    md_3.run_direct(duty_cycle_sp = 50)
    sleep(5)
    mb_3.stop( stop_action = 'brake')
    md_3.stop( stop_action = 'brake')
    mb_3.position = 0
    md_3.position = 0


def downL():
    mb_3.position = 0
    md_3.position = 0
    mb_3.run_direct(duty_cycle_sp = -50)
    md_3.run_direct(duty_cycle_sp = -50)
    sleep(5)
    mb_3.stop( stop_action = 'brake')
    md_3.stop( stop_action = 'brake')
    mb_3.position = 0
    md_3.position = 0

# def Back_Station():
#     ma.position = 0
#     md.position = 0
#     while (mb.position) < -600:
#         ma.run_direct(duty_cycle_sp = -80)
#         md.run_direct(duty_cycle_sp = -80)
#     ma.stop( stop_action = 'brake')
#     md.stop( stop_action = 'brake')
#     ma.position = 0
#     md.position = 0


def upP():
    mc_3.position = 0
    ma_3.position = 0
    mc_3.run_direct(duty_cycle_sp = 50)
    ma_3.run_direct(duty_cycle_sp = 50)
    sleep(5)
    mc_3.stop( stop_action = 'brake')
    ma_3.stop( stop_action = 'brake')
    mc_3.position = 0
    ma_3.position = 0


def downP():
    mc_3.position = 0
    ma_3.position = 0
    mc_3.run_direct(duty_cycle_sp = -50)
    ma_3.run_direct(duty_cycle_sp = -50)
    sleep(5)
    mc_3.stop( stop_action = 'brake')
    ma_3.stop( stop_action = 'brake')
    mc_3.position = 0
    ma_3.position = 0


# def X(x):
#     md.position = 0
#     ma.position = 0
#     while (ma.position) < x*3:
#         ma.run_direct(duty_cycle_sp = 100)
#         md.run_direct(duty_cycle_sp = 100)
#     ma.stop( stop_action = 'brake')
#     md.stop( stop_action = 'brake')
#     md.position = 0
#     ma.position = 0


# def Y(y):
#     md.position = 0
#     ma.position = 0
#     while (ma.position) > -y*3.3:
#         ma.run_direct(duty_cycle_sp = -100)
#         md.run_direct(duty_cycle_sp = -100)
#     ma.stop( stop_action = 'brake')
#     md.stop( stop_action = 'brake')
#     md.position = 0
#     ma.position = 0

def LevoLevo():
    md_2.position = 0
    ma_2.position = 0
    GO = GY.value()
    while GY.value() < (GO +  76):
        md_2.run_direct(duty_cycle_sp = -75)
        ma_2.run_direct(duty_cycle_sp = -75)
        mc_2.run_direct(duty_cycle_sp = 75)
        mb_2.run_direct(duty_cycle_sp = 75)
        sleep(0.05)                                                                            
    ma_2.stop( stop_action = 'brake')
    mb_2.stop( stop_action = 'brake')
    mc_2.stop( stop_action = 'brake')
    md_2.stop( stop_action = 'brake')
    ma_2.position = 0
    mb_2.position = 0
    mc_2.position = 0
    md_2.position = 0
    print(GY.value())

def PravoPravo():
    md_2.position = 0
    ma_2.position = 0
    GO = GY.value()
    while GY.value() > (GO -  75):
        md_2.run_direct(duty_cycle_sp = 75)
        ma_2.run_direct(duty_cycle_sp = 75)
        mc_2.run_direct(duty_cycle_sp = -75)
        mb_2.run_direct(duty_cycle_sp = -75)
        sleep(0.05)                                                                            
    ma_2.stop( stop_action = 'brake')
    mb_2.stop( stop_action = 'brake')
    mc_2.stop( stop_action = 'brake')
    md_2.stop( stop_action = 'brake')
    ma_2.position = 0
    mb_2.position = 0
    mc_2.position = 0
    md_2.position = 0
    print(GY.value())

def Rasvorot():
    md_2.position = 0
    ma_2.position = 0
    GO = GY.value()
    while GY.value() > (GO -  170):
        md_2.run_direct(duty_cycle_sp = 75)
        ma_2.run_direct(duty_cycle_sp = 75)
        mc_2.run_direct(duty_cycle_sp = -75)
        mb_2.run_direct(duty_cycle_sp = -75)
        sleep(0.05)                                                                            
    ma_2.stop( stop_action = 'brake')
    mb_2.stop( stop_action = 'brake')
    mc_2.stop( stop_action = 'brake')
    md_2.stop( stop_action = 'brake')
    ma_2.position = 0
    mb_2.position = 0
    mc_2.position = 0
    md_2.position = 0
    print(GY.value())


    
      

# def StationBack():
#     md.position = 0
#     ma.position = 0
#     while md.position > -2100:
#         ma.run_direct(duty_cycle_sp = -100)
#         md.run_direct(duty_cycle_sp = -100)
#         print(md.position)
#     ma.stop( stop_action = 'brake')
#     md.stop( stop_action = 'brake')
#     md.position = 0
#     ma.position = 0
   


      
      

# # грамма

# print('Press Button')
# while(ts.is_pressed == False):
#     print('Press Button')
#     sleep(00.1)
    
# print("prestart")    
try:
   #if __name__ == '__main__':
#     print("start")
#     speed_counter_Thread = Thread(target=speed_counter_fast)
#     speed_counter_Thread.start()
    
#     mb_1.position, mc_1.position = 0, 0
#     while speed < 1:
#         mb_1.run_direct(duty_cycle_sp = 80)
#         mc_1.run_direct(duty_cycle_sp = 80)
#     mb_1.stop( stop_action = 'brake')
#     mc_1.stop( stop_action = 'brake')
#     b_x, c_x = mb_1.position, mc_1.position
#     time.sleep(1)
    
#     Levo()

#     mWind.position = 0
#     while mWind.position > -65:
#         mWind.run_direct(duty_cycle_sp = -100)
#     mWind.stop(stop_action = 'brake')
    
#     sleep(1.5)
#     Forward()
#     b_y, c_y = mb_1.position, mc_1.position
#     print(b_x,c_x,b_y,c_y)
#     sleep(1.5)
#     Levo()
#     mb_1.position = 0
#     mc_1.position = 0
#     while (mb_1.position) < b_x + 1000:
#         mb_1.run_direct(duty_cycle_sp = 80)
#         mc_1.run_direct(duty_cycle_sp = 80)
#     mb_1.stop( stop_action = 'brake')
#     mc_1.stop( stop_action = 'brake')


#     print(1)
#     sleep(1)  
#     print(2)
#     sleep(1)
#     print(3)
#     sleep(1)
#     print(4)
#     sleep(1)  
#     print(5)
#     sleep(1)
#     print(6)
#     sleep(1)
#     print(7)
#     sleep(1)
#     sleep(9)
      
#     md.position = 0
#     ma.position = 0
#     while (ma.position < 2600):
#         ma.run_direct(duty_cycle_sp = 100)
#         md.run_direct(duty_cycle_sp = 100)
#         sleep(5)
#         print(ma.position)
#     ma.stop( stop_action = 'brake')
#     md.stop( stop_action = 'brake')
#     md.position = 0
#     ma.position = 0
#     X(abs(b_x))

#     time.sleep(2)
#     StationPrav()
#     time.sleep(1)
#     Y(abs(b_y))
#     time.sleep(2)
#     print("I am in needed position")
#     downP()
#     print(1)
#     sleep(1)  
#     print(2)
#     sleep(1)
#     print(3)
#     sleep(1)
#     print(4)
#     sleep(1)  
#     print(5)
#     sleep(1)
#     print(6)
#     sleep(1)
#     print(7)
#     sleep(1)  
    
#     sleep(4)
    
#     while ma.position < b_y*3:
#         ma.run_direct(duty_cycle_sp = 100)
#         md.run_direct(duty_cycle_sp = 100)
#     ma.stop( stop_action = 'brake')
#     md.stop( stop_action = 'brake')
#     md.position = 0
#     ma.position = 0
#     sleep(7)
#     StationLevo()
#     while (md.position) < b_x*3.3  + 1000:
#         ma.run_direct(duty_cycle_sp = -100)
#         md.run_direct(duty_cycle_sp = -100)
#     ma.stop( stop_action = 'brake')
#     md.stop( stop_action = 'brake')
#     md.position = 0
#     ma.position = 0
#     while (md.position) <  1000:
#         ma.run_direct(duty_cycle_sp = -100)
#         md.run_direct(duty_cycle_sp = -100)
#     ma.stop( stop_action = 'brake')
#     md.stop( stop_action = 'brake')
#     md.position = 0
#     ma.position = 0
#     ###############
#     sleep(4)

#     Rasvorot()

#     md.position = 0
#     ma.position = 0
#     while  md.position < 575:
#         ma.run_direct(duty_cycle_sp = -100)
#         md.run_direct(duty_cycle_sp = -100)
#     ma.stop( stop_action = 'brake')
#     md.stop( stop_action = 'brake')
    



#     md.position = 0
#     ma.position = 0
#     while Sony1.value() > 400:
#         ma.run_direct(duty_cycle_sp = -100)
#         md.run_direct(duty_cycle_sp = -100)
#     sleep(0.05)
#     print(Sony1.value())
#     #ma.run_direct(duty_cycle_sp = -100)
#     #md.run_direct(duty_cycle_sp = -100)
#     #sleep(1.5)

#     M = md.position
#     while md.position < (M +  600):
#         md.run_direct(duty_cycle_sp = -100)
#         ma.run_direct(duty_cycle_sp = -100)
#     md.stop( stop_action = 'brake')
#     ma.stop( stop_action = 'brake')
#     ma.position = 0
#     md.position = 0

#     MDX = md.position
#     ma.stop( stop_action = 'brake')
#     md.stop( stop_action = 'brake')
#     md.position = 0
#     ma.position = 0
#     LevoLevo()
#     while T.value() < 1 :
#         ma.run_direct(duty_cycle_sp = 100)
#         md.run_direct(duty_cycle_sp = 100)
#     MDY = md.position
#     ma.stop( stop_action = 'brake')
#     md.stop( stop_action = 'brake')
#     md.position = 0
#     ma.position = 0
#     mb.run_direct(duty_cycle_sp = 45)
#     sleep(7)
#     mb.run_direct(duty_cycle_sp = 100)
#     sleep(5)
#     mb.stop( stop_action = 'brake')
#     mb.position = 0
#     sleep(1)
#     while md.position < -MDY:
#         ma.run_direct(duty_cycle_sp = -100)
#         md.run_direct(duty_cycle_sp = -100)
#     ma.stop( stop_action = 'brake')
#     md.stop( stop_action = 'brake')
#     md.position = 0
#     ma.position = 0
#     # PravoPravo()
#     # while ma.position < MDX:
#     #     ma.run_direct(duty_cycle_sp = 100)
#     #     md.run_direct(duty_cycle_sp = 100)
#     # ma.stop( stop_action = 'brake')
#     # md.stop( stop_action = 'brake')
#     # md.position = 0
#     # ma.position = 0
#     # print(1)
#     # sleep(1)
#     # print(2)
#     # sleep(1)
#     # print(3)
#     # sleep(1)
#     # print(4)
    # md_2.run_direct(duty_cycle_sp = -100)
    # ma_2.run_direct(duty_cycle_sp = 100)
    # mc_2.run_direct(duty_cycle_sp = 100)
    # mb_2.run_direct(duty_cycle_sp = -100)
    # print(GY.value())
    # LevoLevo()
    # PravoPravo()
    # Rasvorot()
    upP()

except KeyboardInterrupt:
    mWind.stop( stop_action = 'brake')
    mb_1.stop( stop_action = 'brake')
    mc_1.stop( stop_action = 'brake')
    mb_1.reset()
    mc_1.reset()   
    mWind.reset()
    sys.exit(1)



# def speed_counter():
#     global speed
#     cl.mode = 'COL-REFLECT'
#     new_color, old_color = 1, 1
#     count, rotation = 0, 0
#     start_time_of_rotation = 0
#     end_time_of_rotation = 0
