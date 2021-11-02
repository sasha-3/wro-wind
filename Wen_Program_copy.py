
#!/usr/bin/env python3
# from Station import Razvorot
import cv2
from threading import Thread
import time, math, os, sys
from time import sleep
from math import sqrt, acos, degrees
import numpy as np
from coords import toInt, add
from sys import argv, platform
from math import sqrt, acos, degrees
import rpyc
global angle_alpha

if __name__ == '__main__':
    def callback(*arg):
        print (arg)




ev3_host_2 = "192.168.1.191"
ev3_host_3 = "192.168.1.195"



ev3_connection_2 = rpyc.classic.connect(ev3_host_2)
ev3_connection_3 = rpyc.classic.connect(ev3_host_3)



ev3dev2_motor_2 = ev3_connection_2.modules['ev3dev2.motor']
ev3dev2_motor_3 = ev3_connection_3.modules['ev3dev2.motor']


ev3dev2_sensor_2 = ev3_connection_2.modules['ev3dev2.sensor']
ev3dev2_sensor_3 = ev3_connection_3.modules['ev3dev2.sensor']



ev3dev2_sensor_lego_2 = ev3_connection_2.modules['ev3dev2.sensor.lego']
ev3dev2_sensor_lego_3 = ev3_connection_3.modules['ev3dev2.sensor.lego']

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


import threading
import cv2
import numpy as np
from numpy import ones,vstack
from numpy.linalg import lstsq
import math


from coords import toInt, add
from sys import argv


cap = cv2.VideoCapture(1)
def photo(q):
    global cap
    # cv2.namedWindow( "result_darkGreen" )
    # cv2.namedWindow( "result_lightGreen" )
    while True:
        
        # HSV фильтр для зеленых объектов из прошлого урока
        hsv_min_lightGreen = np.array((27, 78, 107), np.uint8)
        hsv_max_lightGreen = np.array((35, 255, 255), np.uint8)

        hsv_min_darkGreen = np.array((70, 104, 64), np.uint8)
        hsv_max_darkGreen = np.array((90, 203, 96), np.uint8)

        hsv_min_purple = np.array((107, 92, 52), np.uint8)
        hsv_max_purple = np.array((127, 131, 131), np.uint8)

        x_darkGreen, x_lightGreen, y_darkGreen, y_lightGreen ,x_purple ,y_purple = np.nan,np.nan,np.nan,np.nan,np.nan,np.nan
        flag, img_lightGreen = cap.read()
        flag, img_darkGreen = flag, img_lightGreen
        flag, img = flag, img_lightGreen
        flag, img_purple =  flag, img_lightGreen
        # преобразуем RGB картинку в HSV модель
        hsv_lightGreen = cv2.cvtColor(img_lightGreen, cv2.COLOR_BGR2HSV)
        hsv_darkGreen = cv2.cvtColor(img_darkGreen, cv2.COLOR_BGR2HSV)
        hsv_purple = cv2.cvtColor(img_purple, cv2.COLOR_BGR2HSV)
        # применяем цветовой фильтр
        thresh_lightGreen = cv2.inRange(hsv_lightGreen, hsv_min_lightGreen, hsv_max_lightGreen)
        thresh_darkGreen = cv2.inRange(hsv_darkGreen, hsv_min_darkGreen, hsv_max_darkGreen)
        thresh_purple = cv2.inRange(hsv_purple, hsv_min_purple, hsv_max_purple)
        
        # вычисляем моменты изображения
        moments_lightGreen = cv2.moments(thresh_lightGreen, 1)
        bM01 = moments_lightGreen['m01']
        bM10 = moments_lightGreen['m10']
        bArea = moments_lightGreen['m00']

        moments_purple = cv2.moments(thresh_purple, 1)
        gM01 = moments_purple['m01']
        gM10 = moments_purple['m10']
        gArea = moments_purple['m00']

        moments_darkGreen = cv2.moments(thresh_darkGreen, 1)
        rM01 = moments_darkGreen['m01']
        rM10 = moments_darkGreen['m10']
        rArea = moments_darkGreen['m00']
        # будем реагировать только на те моменты,
        # которые содержать больше 100 пикселей
        if bArea > 100:
            x_lightGreen = int(bM10 / bArea)
            y_lightGreen = int(bM01 / bArea)
            cv2.circle(img_lightGreen, (x_lightGreen, y_lightGreen), 5, (0,0,255), -1)
            cv2.imshow('mask_lightGreen',thresh_lightGreen)
        cv2.imshow('result_lightGreen', img_lightGreen) 
        cv2.imshow('mask_lightGreen',thresh_lightGreen)

        if gArea > 100:
            x_purple = int(gM10 / gArea)
            y_purple = int(gM01 / gArea)
            cv2.circle(img_purple, (x_purple, y_purple), 5, (0,0,255), -1)
            cv2.imshow('mask_purple',thresh_purple)
        cv2.imshow('result_purple', img_purple) 
        cv2.imshow('mask_purple',thresh_purple)

        if rArea > 100:
            x_darkGreen = int(rM10 / rArea)
            y_darkGreen = int(rM01 / rArea)
            cv2.circle(img_darkGreen, (x_darkGreen, y_darkGreen), 5, (0,0,255), -1)
            cv2.imshow('mask_darkGreen',thresh_darkGreen)
        cv2.imshow('result_darkGreen', img_darkGreen) 
        cv2.imshow('mask_darkGreen',thresh_darkGreen)
        # cv2.line(img_all, (x_darkGreen, y_darkGreen), (x_lightGreen, y_lightGreen), (0, 225, 0), 5)


        # img_all = cv2.addWeighted(img_lightGreen, 0.5, img_darkGreen, 0.5, 0.0)
        if  not (np.isnan(x_lightGreen) or np.isnan(y_lightGreen)):
            cv2.circle(img, (x_lightGreen, y_lightGreen), 5, (0,0,255), -1)
        
        if  not (np.isnan(x_darkGreen) or np.isnan(y_darkGreen)):
            cv2.circle(img, (x_darkGreen, y_darkGreen), 5, (0,255,0), -1)

        if  not (np.isnan(x_purple) or np.isnan(y_purple)):
            cv2.circle(img, (x_purple, y_purple), 5, (255,0,0), -1)

        # cv2.line(img, (x_lightGreen, y_lightGreen), (x_darkGreen, y_darkGreen), (0, 255, 0), 2)
        cv2.imshow('mask', img)
        q.put([x_lightGreen,y_lightGreen,x_darkGreen,y_darkGreen,x_purple,y_purple])
        # x = (x_darkGreen + x_lightGreen)/2
        # y = (y_darkGreen + y_lightGreen)/2
        # cv2.circle(img_darkGreen, (x, y), 7, (0,0,225), -1)


        ch = cv2.waitKey(5)
        if ch == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

# def points2tri(x, y, x1, y1):
#     #express coordinates of the point (x2, y2) with respect to point (x1, y1)
#     dx = x1 - x
#     dy = y1 - y

#     alpha = 60./180*math.pi
#     #rotate the displacement vector and add the result back to the original point
#     xp = x1 + math.cos( alpha)*dx + math.sin(alpha)*dy
#     yp = y1 + math.sin(-alpha)*dx + math.cos(alpha)*dy

#     return xp, yp

import queue
q = queue.Queue()
cameraThread = threading.Thread(target=photo,args=(q,))
cameraThread.start()

def calcLength(x0,y0,y1,x1):
    return sqrt(pow(x1-x0,2) + pow(y1-y0,2))

def calcAngle(x0,y0,x1,y1,x2,y2):
    l01 = calcLength(x0,y0,x1,y1)
    l12 = calcLength(x1,y1,x2,y2)
    # print(l01,l12)
    return ((x0 - x1)*(x2-x1) + (y0-y1)*(y2-y1)) / (l01*l12)  

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
#Функции для робота-установщик

def downL():
    mb_3.position = 0
    md_3.position = 0
    mb_3.run_direct(duty_cycle_sp = -15)
    md_3.run_direct(duty_cycle_sp = -15)
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

#Функции для робота-установщик
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

#Функции для робота-установщик
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

# #Функции для установщик
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

# #Функции для установщик
def PravoPravo():
    md_2.position = 0
    ma_2.position = 0
    GO = GY.value()
    while GY.value() > (GO -  88):
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

# #Функции для установщик
def Rasvorot():
    md_2.position = 0
    ma_2.position = 0
    GO = GY.value()
    while GY.value() > (GO -  172):
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
   


      
      

# грамма







ma_2.position = 0
mb_2.position = 0
mc_2.position = 0
md_2.position = 0

while mc_2.position < 6000:
        md_2.run_direct(duty_cycle_sp = -75)
        ma_2.run_direct(duty_cycle_sp = 75)
        mc_2.run_direct(duty_cycle_sp = 75)
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
PravoPravo()



ma_2.position = 0
mb_2.position = 0
mc_2.position = 0
md_2.position = 0

while md_2.position < 3500:
        md_2.run_direct(duty_cycle_sp = 75)
        ma_2.run_direct(duty_cycle_sp = -75)
        mc_2.run_direct(duty_cycle_sp = -75)
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
downL()
sleep(5)
ma_2.position = 0
mb_2.position = 0
mc_2.position = 0
md_2.position = 0

while ma_2.position < 3500:
        md_2.run_direct(duty_cycle_sp = -75)
        ma_2.run_direct(duty_cycle_sp = 75)
        mc_2.run_direct(duty_cycle_sp = 75)
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
PravoPravo()
ma_2.position = 0
mb_2.position = 0
mc_2.position = 0
md_2.position = 0

while ma_2.position < 6000:
        md_2.run_direct(duty_cycle_sp = -75)
        ma_2.run_direct(duty_cycle_sp = 75)
        mc_2.run_direct(duty_cycle_sp = 75)
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

sleep(8)
Rasvorot()
ma_2.position = 0
mb_2.position = 0
mc_2.position = 0
md_2.position = 0

while mc_2.position < 6000:
        md_2.run_direct(duty_cycle_sp = -75)
        ma_2.run_direct(duty_cycle_sp = 75)
        mc_2.run_direct(duty_cycle_sp = 75)
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
LevoLevo()
ma_2.position = 0
mb_2.position = 0
mc_2.position = 0
md_2.position = 0

while ma_2.position < 3500:
        md_2.run_direct(duty_cycle_sp = -75)
        ma_2.run_direct(duty_cycle_sp = 75)
        mc_2.run_direct(duty_cycle_sp = 75)
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










#         print(q.get())
#         x_lightGreen = q.get()[0]
#         y_lightGreen = q.get()[1]
#         x_darkGreen = q.get()[2]
#         y_darkGreen = q.get()[3]
#         x_purple = q.get()[4]
#         y_purple = q.get()[5]
        
#         # line_equation(points=[(q.get()[0], q.get()[1]), (q.get()[2], q.get()[3])])

#         if (stage == "turn"):

#         # координаты A - центр робота
#         # x_darkGreen 
#         # y_darkGreen 
#         # координаты B - перед робота
#         # x_lightGreen 
#         # y_lightGreen
#         # координаты C - куда надо повернуться
#         # y_purple
#         # x_purple
            

#             c = sqrt((x_darkGreen-x_lightGreen)*(x_darkGreen-x_lightGreen) + (y_darkGreen-y_lightGreen)*(y_darkGreen-y_lightGreen))
#             b = sqrt((x_darkGreen-x_purple)*(x_darkGreen-x_purple) + (y_darkGreen-y_purple)*(y_darkGreen-y_purple))
#             a = sqrt((x_purple-x_lightGreen)*(x_purple-x_lightGreen) + (y_purple-y_lightGreen)*(y_purple-y_lightGreen))

#             # print(a, b, c)

#             a2 = a*a
#             b2 = b*b
#             c2 = c*c

            
#             t = (x_lightGreen*x_purple+ y_lightGreen*y_purple)/(((x_lightGreen*x_lightGreen+ y_lightGreen* y_lightGreen)**0.5)*((x_purple*+y_purple*y_purple)**0.5))

#             q = 1.5707963267 - round(math.acos(t),6)
#             w = round(math.acos(t),6)
#             print(t,q,w)
# # if q < w:
# #     print(q)
# # else:
# #     print(w)


#             angle_alpha = degrees(acos((b2+c2-a2)/(2*b*c)))
#             # angle_alpha = calcAngle(x_darkGreen,y_darkGreen,x_lightGreen,y_lightGreen,x_purple,y_purple)
#             print(angle_alpha)


#             # ошибка для регулятора
#             k = 0.8
#             # error = angle_alpha - 0
#             # u = k*error


#             # md_2.run_direct(duty_cycle_sp = -u)
#             # ma_2.run_direct(duty_cycle_sp = -u)
#             # mc_2.run_direct(duty_cycle_sp = u)
#             # mb_2.run_direct(duty_cycle_sp = u)

#             # if (abs(error) < 15):
#                 # stage = "move"                                                                  
            
#             print(GY.value())
#             sleep(0.5)
        
#         elif (stage == "move"):
#             exit()

      
#     except KeyboardInterrupt:
#         sys.exit(1)
      
            
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

    #         md_2.position = 0
    #         ma_2.position = 0
    #         GO = GY.value()
    #             while GY.value() < (GO +  76):
    #         md_2.run_direct(duty_cycle_sp = -75)
    #         ma_2.run_direct(duty_cycle_sp = -75)
    #         mc_2.run_direct(duty_cycle_sp = 75)
    #         mb_2.run_direct(duty_cycle_sp = 75)                                                                            
    #     ma_2.stop( stop_action = 'brake')
    #     mb_2.stop( stop_action = 'brake')
    #     mc_2.stop( stop_action = 'brake')
    #     md_2.stop( stop_action = 'brake')
    #     ma_2.position = 0
    #     mb_2.position = 0
    #     mc_2.position = 0
    #     md_2.position = 0
    #     print(GY.value())
    # #     X(abs(b_x))

    #     time.sleep(2)
    #     StationPrav()
    #     time.sleep(1)
    #     Y(abs(b_y))
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
        # upP()
     

# def speed_counter():
#     global speed
#     cl.mode = 'COL-REFLECT'
#     new_color, old_color = 1, 1
#     count, rotation = 0, 0
#     start_time_of_rotation = 0
#     end_time_of_rotation = 0
