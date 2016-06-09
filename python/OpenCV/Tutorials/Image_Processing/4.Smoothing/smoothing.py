import cv2
import numpy as np 
from matplotlib import pyplot as plt

image_path = '/Users/e145735/Documents/opencv_samples/'

img = cv2.imread(image_path + 'opencv_logo.jpg')

median = cv2.medianBlur(img,5)
#blur = cv2.blur(img,(5,5))
#blur = cv2.GaussianBlur(img,(5,5),0)
blur = cv2.bilateralFilter(img,9,75,75)

plt.subplot(121),plt.imshow(median),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]),plt.yticks([])
plt.show()