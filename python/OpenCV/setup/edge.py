#!/usr/bin/env python

import cv2

def main():
	img = cv2.imread('image.png',0)
	edge_img = cv2.Canny(img,100,200)
	cv2.imshow('python',edge_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()