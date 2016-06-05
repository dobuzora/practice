import cv2
import numpy as np

image_path = 'FULL_PATH'

img = cv2.imread(image_path + 'messi5.jpg',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()