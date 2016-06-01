#!/usr/bin/env python

import cv2

def main():
	img = cv2.imread('image.png')
	cv2.imshow('python',img)
	cv2.waitKey(0)
	cv2.destroyAllWindow()

if __name__ == '__main__':
	main()