import cv2
import numpy as np

image_path="FULL_PATH"

img = cv2.imread(image_path + 'messi5.jpg')

res = cv2.resize(img,None,fx=2,fy=2,interpolation = cv2.INTER_CUBIC)

#OR
#height, width = img.shape[:2]
#res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

cv2.imshow('image',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
