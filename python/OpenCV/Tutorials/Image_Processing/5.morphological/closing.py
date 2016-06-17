import cv2
import numpy as np 
from matplotlib import pyplot as plt

image_path = '/Users/e145735/Documents/opencv_samples/'

img = cv2.imread(image_path + 'j.png',0)
kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('image',closing)
cv2.waitKey(0)
cv2.destroyAllWindows()

