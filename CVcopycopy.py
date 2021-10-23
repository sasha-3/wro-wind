#!/usr/bin/env python3
import cv2
import numpy as np
#import video

cv2.namedWindow( "oio" )
cap = cv2.VideoCapture(0); 


# HSV фильтр для зеленых объектов из прошлого урока
hsv_min = np.array((0,225, 131), np.uint8)
hsv_max = np.array((225, 225, 255), np.uint8)

while True:
    red_img = img.copy()
    x_size = img.shape[1]
    y_size = img.shape[0]
    red_points = 0
    for y in range(y_size):
        for x in range(x_size):
            point_blue = img[y,x,0]
            point_green = img[y,x,1]
            point_red = img[y,x,2]
            red_img[y,x,0] = 0
            red_img[y,x,1] = 0
            red_img[y,x,2] = 0
            if (point_red > 18) and (point_green < 10) and (point_blue < 143):
                red_points += 1
                red_img[y,x,2] = 255
    flag, img = cap.read()
    # преобразуем RGB картинку в HSV модель
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
    # применяем цветовой фильтр
    thresh = cv2.inRange(hsv, hsv_min, hsv_max)

    # вычисляем моменты изображения




    cv2.imshow('oio', img) 
 
    ch = cv2.waitKey(5)
    if ch == 27:
        break

cap.release()
cv2.destroyAllWindows()