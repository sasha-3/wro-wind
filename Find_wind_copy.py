
#!/usr/bin/env python3
# from Station import Razvorot
from ev3dev.ev3 import *
from threading import Thread
import time, math, os, sys, rpyc
from time import sleep


Station_conn = rpyc.classic.connect('192.168.43.238')

ev3dev2_motor = Station_conn.modules['ev3dev2.motor']
ev3dev2_sensor = Station_conn.modules['ev3dev2.sensor']
ev3dev2_sensor_lego = Station_conn.modules['ev3dev2.sensor.lego']

ma = ev3dev2_motor.LargeMotor(ev3dev2_motor.OUTPUT_A)
mb = ev3dev2_motor.LargeMotor(ev3dev2_motor.OUTPUT_B)  
mc = ev3dev2_motor.LargeMotor(ev3dev2_motor.OUTPUT_C)
md = ev3dev2_motor.LargeMotor(ev3dev2_motor.OUTPUT_D)  
GY = ev3dev2_sensor_lego.GyroSensor(ev3dev2_sensor.INPUT_1)
T = ev3dev2_sensor_lego.TouchSensor(ev3dev2_sensor.INPUT_3)
Sony1 = ev3dev2_sensor_lego.UltrasonicSensor(ev3dev2_sensor.INPUT_2)



speed = 0

mWind = MediumMotor('outD')  
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

def Levo():
    motor_b.position = 0
    motor_c.position = 0
    go = gy.value()
    while gy.value() < (go +  75):
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
def upL():
    mb.position = 0
    while (mb.position) < 430:
        mb.run_direct(duty_cycle_sp = 50)
    mb.stop( stop_action = 'brake')
    mb.position = 0


def downL():
    mb.run_direct(duty_cycle_sp = -30)
    sleep(6)
    mb.stop( stop_action = 'brake')

def Back_Station():
    ma.position = 0
    md.position = 0
    while (mb.position) < -600:
        ma.run_direct(duty_cycle_sp = -80)
        md.run_direct(duty_cycle_sp = -80)
    ma.stop( stop_action = 'brake')
    md.stop( stop_action = 'brake')
    ma.position = 0
    md.position = 0


def upP():
    mc.position = 0
    while (mc.position) < 430:
        mc.run_direct(duty_cycle_sp = 50)
    mc.stop( stop_action = 'brake')
    mc.position = 0


def downP():
    mc.run_direct(duty_cycle_sp = -30)
    sleep(6)
    mc.stop( stop_action = 'brake')


def X(x):
    md.position = 0
    ma.position = 0
    while (ma.position) < x*3:
        ma.run_direct(duty_cycle_sp = 100)
        md.run_direct(duty_cycle_sp = 100)
    ma.stop( stop_action = 'brake')
    md.stop( stop_action = 'brake')
    md.position = 0
    ma.position = 0


def Y(y):
    md.position = 0
    ma.position = 0
    while (ma.position) > -y*3.3:
        ma.run_direct(duty_cycle_sp = -100)
        md.run_direct(duty_cycle_sp = -100)
    ma.stop( stop_action = 'brake')
    md.stop( stop_action = 'brake')
    md.position = 0
    ma.position = 0

def LevoLevo():
    md.position = 0
    ma.position = 0
    GO = GY.value()
    while GY.value() > (GO -  73):
        md.run_direct(duty_cycle_sp = 100)
        ma.run_direct(duty_cycle_sp = -100)
        sleep(0.05)
    md.stop( stop_action = 'brake')
    ma.stop( stop_action = 'brake')
    ma.position = 0
    md.position = 0

def PravoPravo():
    md.position = 0
    ma.position = 0
    GO = GY.value()
    while GY.value() < (GO +  73):
        md.run_direct(duty_cycle_sp = -100)
        ma.run_direct(duty_cycle_sp = 100)
        sleep(0.05)
    md.stop( stop_action = 'brake')
    ma.stop( stop_action = 'brake')
    ma.position = 0
    md.position = 0

def Rasvorot():
    md.position = 0
    ma.position = 0
    GO = GY.value()
    while GY.value() > (GO -  170):
        md.run_direct(duty_cycle_sp = 100)
        ma.run_direct(duty_cycle_sp = -100)
        sleep(0.05)
    md.stop( stop_action = 'brake')
    ma.stop( stop_action = 'brake')
    ma.position = 0
    md.position = 0




def StationLevo():
    md.position = 0
    ma.position = 0
    GO = GY.value()
    while GY.value() < (GO +  70):#Gyro.value() > (GO -  88):
        md.run_direct(duty_cycle_sp = -100)
        ma.run_direct(duty_cycle_sp = 100)
        sleep(0.05)
    md.stop( stop_action = 'brake')
    ma.stop( stop_action = 'brake')
    ma.position = 0
    md.position = 0


def StationPrav():
    md.position = 0
    ma.position = 0
    GO = GY.value()
    while GY.value() > (GO -  75):
        md.run_direct(duty_cycle_sp = 100)
        ma.run_direct(duty_cycle_sp = -100)
        sleep(0.05)
    md.stop( stop_action = 'brake')
    ma.stop( stop_action = 'brake')
    ma.position = 0
    md.position = 0
      

def StationBack():
    md.position = 0
    ma.position = 0
    while md.position > -2100:
        ma.run_direct(duty_cycle_sp = -100)
        md.run_direct(duty_cycle_sp = -100)
        print(md.position)
    ma.stop( stop_action = 'brake')
    md.stop( stop_action = 'brake')
    md.position = 0
    ma.position = 0
   

def StationRazvorot():
    md.position = 0
    ma.position = 0
    while (md.position) < 5000:
        ma.run_direct(duty_cycle_sp = -100)
        md.run_direct(duty_cycle_sp = 100)
    ma.stop( stop_action = 'brake')
    md.stop( stop_action = 'brake')
    md.position = 0
    ma.position = 0
      
      

# грамма

print('Press Button')
while(ts.is_pressed == False):
    print('Press Button')
    sleep(00.1)
    
print("prestart")    
try:
    #if __name__ == '__main__':
    print("start")
    speed_counter_Thread = Thread(target=speed_counter_fast)
    speed_counter_Thread.start()
    
    motor_b.position, motor_c.position = 0, 0
    while speed < 1:
        motor_b.run_direct(duty_cycle_sp = 80)
        motor_c.run_direct(duty_cycle_sp = 80)
    motor_b.stop( stop_action = 'brake')
    motor_c.stop( stop_action = 'brake')
    b_x, c_x = motor_b.position, motor_c.position
    time.sleep(1)
    
    Levo()

    mWind.position = 0
    while mWind.position > -65:
        mWind.run_direct(duty_cycle_sp = -100)
    mWind.stop(stop_action = 'brake')
    
    sleep(1.5)
    Forward()
    b_y, c_y = motor_b.position, motor_c.position
    print(b_x,c_x,b_y,c_y)
    sleep(1.5)
    Levo()
    motor_b.position = 0
    motor_c.position = 0
    while (motor_b.position) < b_x + 1000:
        motor_b.run_direct(duty_cycle_sp = 80)
        motor_c.run_direct(duty_cycle_sp = 80)
    motor_b.stop( stop_action = 'brake')
    motor_c.stop( stop_action = 'brake')


    print(1)
    sleep(1)  
    print(2)
    sleep(1)
    print(3)
    sleep(1)
    print(4)
    sleep(1)  
    print(5)
    sleep(1)
    print(6)
    sleep(1)
    print(7)
    sleep(1)
    sleep(9)
      
    md.position = 0
    ma.position = 0
    while (ma.position < 2600):
        ma.run_direct(duty_cycle_sp = 100)
        md.run_direct(duty_cycle_sp = 100)
        sleep(5)
        print(ma.position)
    ma.stop( stop_action = 'brake')
    md.stop( stop_action = 'brake')
    md.position = 0
    ma.position = 0
    X(abs(b_x))

    time.sleep(2)
    StationPrav()
    time.sleep(1)
    Y(abs(b_y))
    time.sleep(2)
    print("I am in needed position")
    downP()
    print(1)
    sleep(1)  
    print(2)
    sleep(1)
    print(3)
    sleep(1)
    print(4)
    sleep(1)  
    print(5)
    sleep(1)
    print(6)
    sleep(1)
    print(7)
    sleep(1)  
    
    sleep(4)
    
    while ma.position < b_y*3:
        ma.run_direct(duty_cycle_sp = 100)
        md.run_direct(duty_cycle_sp = 100)
    ma.stop( stop_action = 'brake')
    md.stop( stop_action = 'brake')
    md.position = 0
    ma.position = 0
    sleep(7)
    StationLevo()
    while (md.position) < b_x*3.3  + 1000:
        ma.run_direct(duty_cycle_sp = -100)
        md.run_direct(duty_cycle_sp = -100)
    ma.stop( stop_action = 'brake')
    md.stop( stop_action = 'brake')
    md.position = 0
    ma.position = 0
    while (md.position) <  1000:
        ma.run_direct(duty_cycle_sp = -100)
        md.run_direct(duty_cycle_sp = -100)
    ma.stop( stop_action = 'brake')
    md.stop( stop_action = 'brake')
    md.position = 0
    ma.position = 0
    ###############
    sleep(4)

    Rasvorot()

    md.position = 0
    ma.position = 0
    while  md.position < 575:
        ma.run_direct(duty_cycle_sp = -100)
        md.run_direct(duty_cycle_sp = -100)
    ma.stop( stop_action = 'brake')
    md.stop( stop_action = 'brake')
    



    md.position = 0
    ma.position = 0
    while Sony1.value() > 400:
        ma.run_direct(duty_cycle_sp = -100)
        md.run_direct(duty_cycle_sp = -100)
    sleep(0.05)
    print(Sony1.value())
    #ma.run_direct(duty_cycle_sp = -100)
    #md.run_direct(duty_cycle_sp = -100)
    #sleep(1.5)

    M = md.position
    while md.position < (M +  600):
        md.run_direct(duty_cycle_sp = -100)
        ma.run_direct(duty_cycle_sp = -100)
    md.stop( stop_action = 'brake')
    ma.stop( stop_action = 'brake')
    ma.position = 0
    md.position = 0

    MDX = md.position
    ma.stop( stop_action = 'brake')
    md.stop( stop_action = 'brake')
    md.position = 0
    ma.position = 0
    LevoLevo()
    while T.value() < 1 :
        ma.run_direct(duty_cycle_sp = 100)
        md.run_direct(duty_cycle_sp = 100)
    MDY = md.position
    ma.stop( stop_action = 'brake')
    md.stop( stop_action = 'brake')
    md.position = 0
    ma.position = 0
    mb.run_direct(duty_cycle_sp = 45)
    sleep(7)
    mb.run_direct(duty_cycle_sp = 100)
    sleep(5)
    mb.stop( stop_action = 'brake')
    mb.position = 0
    sleep(1)
    while md.position < -MDY:
        ma.run_direct(duty_cycle_sp = -100)
        md.run_direct(duty_cycle_sp = -100)
    ma.stop( stop_action = 'brake')
    md.stop( stop_action = 'brake')
    md.position = 0
    ma.position = 0
    # PravoPravo()
    # while ma.position < MDX:
    #     ma.run_direct(duty_cycle_sp = 100)
    #     md.run_direct(duty_cycle_sp = 100)
    # ma.stop( stop_action = 'brake')
    # md.stop( stop_action = 'brake')
    # md.position = 0
    # ma.position = 0
    # print(1)
    # sleep(1)
    # print(2)
    # sleep(1)
    # print(3)
    # sleep(1)
    # print(4)

except KeyboardInterrupt:
    mWind.stop( stop_action = 'brake')
    motor_b.stop( stop_action = 'brake')
    motor_c.stop( stop_action = 'brake')
    motor_b.reset()
    motor_c.reset()   
    mWind.reset()
    sys.exit(1)



# def speed_counter():
#     global speed
#     cl.mode = 'COL-REFLECT'
#     new_color, old_color = 1, 1
#     count, rotation = 0, 0
#     start_time_of_rotation = 0
#     end_time_of_rotation = 0
