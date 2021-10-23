from cv2 import cv2
import numpy as np
cap = cv2.VideoCapture(1)

def nothing(x): #  Пустая функция
      pass
cv2.namedWindow("Tracking")
cv2.createTrackbar("r_l", "Tracking", 0, 255, nothing) # создание элемента  Trackbar
cv2.createTrackbar("g_l", "Tracking", 0, 255, nothing)
cv2.createTrackbar("b_l", "Tracking", 0, 255, nothing)
cv2.createTrackbar("r_h", "Tracking", 255, 255, nothing)
cv2.createTrackbar("g_h", "Tracking", 255, 255, nothing)
cv2.createTrackbar("b_h", "Tracking", 255, 255, nothing)    
r_l = cv2.getTrackbarPos("r_l", "Tracking")
g_l = cv2.getTrackbarPos("g_l", "Tracking")
b_l = cv2.getTrackbarPos("b_l", "Tracking")

r_h = cv2.getTrackbarPos("r_h", "Tracking")
g_h = cv2.getTrackbarPos("g_h", "Tracking")
b_h = cv2.getTrackbarPos("b_h", "Tracking")
while True:
    _, img = cap.read()
 
    #percent by which the image is resized
    scale_percent = 20
 
    #calculate the 20 percent of original dimensions
    width = int(img.shape[1] * scale_percent / 35)
    height = int(img.shape[0] * scale_percent / 35)
 
    # dsize
    dsize = (width, height)
    

  

 
    # resize image
    img = cv2.resize(img, dsize)
 
    # blur image
    #img = cv2.blur(img,(1,1))
 
    blue_img = img.copy()
    x_size = img.shape[1]
    y_size = img.shape[0]
    blue_points = 0
    for y in range(y_size):
        for x in range(x_size):
            point_blue = img[y,x,0]
            point_green = img[y,x,1]
            point_red = img[y,x,2]
            if (r_l<point_red<r_h ) and (g_l<point_green<g_h) and (b_l<point_blue<b_h):
                blue_points += 1
                blue_img[y,x,0] = 255
                blue_img[y,x,1] = 255
                blue_img[y,x,2] = 255
 
    
    print(blue_points)

 
    cv2.imshow("red_img", blue_img)
    # cv2.imshow("camera", img)
 
    if cv2.waitKey(10) == 27: # Клавиша Esc
        break
cap.release()
cv2.destroyAllWindows() 