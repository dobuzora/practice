import numpy as np
import cv2

# イメージ画像フォルダへのフルパス
image_path = "FULL_PATH"

### Read an image
img = cv2.imread(image_path + 'messi5.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
print(k)
if k == 27: # ESCキーの時
	cv2.destroyAllWindows()
elif k == ord('s'): # s が押された時
	# ファイルに書き込む
	cv2.imwrite('messigray.png',img)
	cv2.destroyAllWindows()