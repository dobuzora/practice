
from __future__ import division

import time

import cv2

def main():
	video = cv2.VideoCapture('movie.mp4')

	fps = video.get(cv2.CAP_PROP_FPS)

	while video.isOpened():
		success,frame = video.read()

		if not success:
			break

		cv2.imshow('video',frame)

		if cv2.waitKey(1) != -1:
			break

		time.sleep(1/fps)

	video.release()
	cv2.destoryAllWindows()

if __name__ == '__main__':
	main()