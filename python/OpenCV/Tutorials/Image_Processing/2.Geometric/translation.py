import cv2
import numpy as np
 
image_path = "FULL_PATH"

img = cv2.imread(image_path + 'messi5.jpg')
rows,cols,n = img.shape

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
