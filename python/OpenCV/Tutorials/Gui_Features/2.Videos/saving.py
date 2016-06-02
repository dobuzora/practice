import numpy as np
import cv2

# 現状動きません！！

# OSXだとできないらしい(ちょこちょこっとするとできるらしい)
# http://www.pyimagesearch.com/2016/02/22/writing-to-video-with-opencv/
# In OSX : *(I don't have access to OSX. Can some one fill this?)*

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()