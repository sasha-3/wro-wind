import cv2
import numpy as np
from coords import toInt, add
from sys import argv

if __name__ == '__main__':
    def callback(*arg):
        print (arg)

cv2.namedWindow( "result_red" )
cv2.namedWindow( "result_blue" )


cap = cv2.VideoCapture(1)
# HSV фильтр для зеленых объектов из прошлого урока
hsv_min_blue = np.array((25, 72, 151), np.uint8)
hsv_max_blue = np.array((48, 108, 195), np.uint8)

hsv_min_red = np.array((79, 88, 96), np.uint8)
hsv_max_red = np.array((90, 163, 225), np.uint8)

while True:
    
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
    cv2.circle(img, (x_blue, y_blue), 5, (0,0,255), -1)
    cv2.circle(img, (x_red, y_red), 5, (0,0,255), -1)


    cv2.line(img, (x_blue, y_blue), (x_red, y_red), (0, 255, 0), 2)


    cv2.imshow('mask', img)

    # x = (x_red + x_blue)/2
    # y = (y_red + y_blue)/2
    # cv2.circle(img_red, (x, y), 7, (0,0,225), -1)


    ch = cv2.waitKey(5)
    if ch == 27:
        break

cap.release()
cv2.destroyAllWindows()