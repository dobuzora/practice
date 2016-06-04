import numpy as np
import cv2

# Create a black image
img = ~np.zeros((512,512,3), np.uint8)

cv2.ellipse(img,(256,100),(100,100),120,0,300,(0,0,255),-1)
cv2.ellipse(img,(366,300),(100,100),300,0,300,(255,0,0),-1)
cv2.ellipse(img,(146,300),(100,100),0,0,300,(0,255,0),-1)

cv2.circle(img,(256,100), 50, (255,255,255), -1)
cv2.circle(img,(366,300), 50, (255,255,255), -1)
cv2.circle(img,(146,300), 50, (255,255,255), -1)


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(0,0,0),8,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()