import cv2
import numpy as np
from matplotlib import pyplot as plt 

image_path = 'FULL_PATH'

img = cv2.imread(image_path + 'opencv_logo.jpg')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()