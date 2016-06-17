import numpy as np
import cv2

im = cv2.imread('test.png')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY)

image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# img = cv2.drawContours(im, contours, -1, (0,255,0), 3)

cnt = contours[2]
img = cv2.drawContours(im, [cnt], 0, (0,255,0), 3)

cv2.imshow("test",thresh)
cv2.waitKey(0)