import cv2
import numpy as np 
from matplotlib import pyplot as plt

image_path = '/Users/e145735/Documents/opencv_samples/'

img = cv2.imread(image_path + 'j.png',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)

cv2.imshow('image',erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()