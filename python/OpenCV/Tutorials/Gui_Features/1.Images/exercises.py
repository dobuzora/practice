import numpy as np
import cv2
from matplotlib import pyplot as plt

# イメージ画像フォルダへのフルパス
image_path = "FULL_PATH"

img = cv2.imread(image_path + 'messi5.jpg',1)
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
plt.imshow(img2)
plt.xticks([]),plt.yticks([])
plt.show()
