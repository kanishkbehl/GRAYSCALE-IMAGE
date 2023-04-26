import cv2
import numpy as num

img = cv2.imread("sample.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("window",img_gray)        #SHOW GRAYSCALE IMAGE
cv2.waitKey(0)             
print(img_gray.shape)               #SHAPE OF IMAGE