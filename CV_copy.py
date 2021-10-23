#!/usr/bin/env python3
 
import cv2
import numpy as np

def nothing(x): #  Пустая функция
      pass

# захват видеопотока с вебкамеры
cap = cv2.VideoCapture(1)


# создаем окно с ползунками

cv2.namedWindow("Tracking")
cv2.createTrackbar("l_h", "Tracking", 0, 255, nothing) # создание элемента  Trackbar
cv2.createTrackbar("l_s", "Tracking", 0, 255, nothing)
cv2.createTrackbar("l_v", "Tracking", 0, 255, nothing)
cv2.createTrackbar("u_h", "Tracking", 255, 255, nothing)
cv2.createTrackbar("u_s", "Tracking", 255, 255, nothing)
cv2.createTrackbar("u_v", "Tracking", 255, 255, nothing)


while True:

    # image = cv2.imread("D:/apple-1112047_1280.jpg") # метод считывает переданную ему строку
 
    _, frame = cap.read()


    # перевод изображения формата BGR в  HSV, формат hsv: hue, saturation, value
   
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   
   
    # продолжение ниже...
     


 # ...продолжение предыдущего кода


    # получение значения элемента Trackbar  
    scale_percent = 20
    width = int(img.shape[1] * scale_percent / 20)
    height = int(img.shape[0] * scale_percent / 20)
 
    # dsize
    dsize = (width, height)
 
    # resize image
    img = cv2.resize(img, dsize)

    LH = cv2.getTrackbarPos("l_h", "Tracking")
    LS = cv2.getTrackbarPos("l_s", "Tracking")
    LV = cv2.getTrackbarPos("l_v", "Tracking")

    UH = cv2.getTrackbarPos("u_h", "Tracking")
    US = cv2.getTrackbarPos("u_s", "Tracking")
    UV = cv2.getTrackbarPos("u_v", "Tracking")

    # первое значение в массиве - hue - цвет, второе - saturation - насыщенность, третье value - яркость
    lower_border = np.array([LH, LS, LV])

    upper_border = np.array([UH, US, UV]) # верхняя граница цветового массива  hsv

    mask = cv2.inRange(hsv, lower_border, upper_border) # маска для нахождения объекта указанного цветового массива на изображении
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
              # окончательный вариант
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

    
    cv2.imshow("color", frame)  # оригинальное фото
    cv2.imshow("mask", mask) # фото после фильтрации по цвету
    cv2.imshow("hsv", hsv) # фото в формате  hsv
    cv2.imshow("res", res)
    

    key = cv2.waitKey(1)
    if key == 27:
        break


cap.release() # запуск видео цикла
cv2.destroyAllWindows() # метод закрытия  всех окон при остановке программы