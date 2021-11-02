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
    
    # cv2.namedWindow( "result_red" )
    # cv2.namedWindow( "result_blue" )
    while True:
        
        # HSV фильтр для зеленых объектов из прошлого урока
        hsv_min_blue = np.array((27, 78, 107), np.uint8)
        hsv_max_blue = np.array((35, 255, 255), np.uint8)

        hsv_min_red = np.array((70, 104, 64), np.uint8)
        hsv_max_red = np.array((90, 203, 96), np.uint8)

        x_red, x_blue, y_red, y_blue = np.nan,np.nan,np.nan,np.nan
        flag, img_blue = cap.read()
        flag, img_red = flag, img_blue
        flag, img = flag, img_blue
        # преобразуем RGB картинку в HSV модель
        hsv_blue = cv2.cvtColor(img_blue, cv2.COLOR_BGR2HSV)
        hsv_red = cv2.cvtColor(img_red, cv2.COLOR_BGR2HSV)
        # применяем цветовой фильтр
        thresh_blue = cv2.inRange(hsv_blue, hsv_min_blue, hsv_max_blue)
        thresh_red = cv2.inRange(hsv_red, hsv_min_red, hsv_max_red)

        # вычисляем моменты изображения
        moments_blue = cv2.moments(thresh_blue, 1)
        bM01 = moments_blue['m01']
        bM10 = moments_blue['m10']
        bArea = moments_blue['m00']


        moments_red = cv2.moments(thresh_red, 1)
        rM01 = moments_red['m01']
        rM10 = moments_red['m10']
        rArea = moments_red['m00']
        # будем реагировать только на те моменты,
        # которые содержать больше 100 пикселей
        if bArea > 100:
            x_blue = int(bM10 / bArea)
            y_blue = int(bM01 / bArea)
            cv2.circle(img_blue, (x_blue, y_blue), 5, (0,0,255), -1)
            cv2.imshow('mask_blue',thresh_blue)
        cv2.imshow('result_blue', img_blue) 
        cv2.imshow('mask_blue',thresh_blue)

        if rArea > 100:
            x_red = int(rM10 / rArea)
            y_red = int(rM01 / rArea)
            cv2.circle(img_red, (x_red, y_red), 5, (0,0,255), -1)
            cv2.imshow('mask_red',thresh_red)
        cv2.imshow('result_red', img_red) 
        cv2.imshow('mask_red',thresh_red)
        # cv2.line(img_all, (x_red, y_red), (x_blue, y_blue), (0, 225, 0), 5)


        # img_all = cv2.addWeighted(img_blue, 0.5, img_red, 0.5, 0.0)
        if  not (np.isnan(x_blue) or np.isnan(y_blue)):
            cv2.circle(img, (x_blue, y_blue), 5, (0,0,255), -1)
        
        if  not (np.isnan(x_red) or np.isnan(y_red)):
            cv2.circle(img, (x_red, y_red), 5, (0,0,255), -1)

        # cv2.line(img, (x_blue, y_blue), (x_red, y_red), (0, 255, 0), 2)
        cv2.imshow('mask', img)
        q.put([x_blue,y_blue,x_red,y_red])
        # x = (x_red + x_blue)/2
        # y = (y_red + y_blue)/2
        # cv2.circle(img_red, (x, y), 7, (0,0,225), -1)


        ch = cv2.waitKey(5)
        if ch == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

def points2tri(x, y, x1, y1):
    #express coordinates of the point (x2, y2) with respect to point (x1, y1)
    dx = x1 - x
    dy = y1 - y

    alpha = 60./180*math.pi
    #rotate the displacement vector and add the result back to the original point
    xp = x1 + math.cos( alpha)*dx + math.sin(alpha)*dy
    yp = y1 + math.sin(-alpha)*dx + math.cos(alpha)*dy

    return xp, yp

import queue
q = queue.Queue()
cameraThread = threading.Thread(target=photo,args=(q,))
cameraThread.start()

while True:
    try:
        print(q.get())
        # line_equation(points=[(q.get()[0], q.get()[1]), (q.get()[2], q.get()[3])])
    except KeyboardInterrupt:
        break
import sys
sys.exit(1)
