import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = 'FULL_PATH'

img = cv2.imread(image_path + 'chessboard.png')
rows,cols,ch = img.shape

pts1 = np.float32([[1000,1000],[3000,1000],[1000,3000],[3000,3000]])
pst2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

# For perspective transformation, you need a 3x3 transformation matrix.
M = cv2.getPerspectiveTransform(pts1,pst2)

# apply cv2.warpPerspective with this 3x3 transformation matrix.
dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()