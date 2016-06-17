import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = '/Users/e145735/Documents/opencv_samples/'


img = cv2.imread(image_path + 'home.jpg')

'''
plt.hist(img.ravel(),256,[0,256])
plt.show()
'''

color = ['b','g','r']
for i ,col in enumerate(color):
	histr = cv2.calcHist([img],[i],None,[256],[0,256])
	plt.plot(histr,color = col)
	plt.xlim([0,256])
plt.show()