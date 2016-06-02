import numpy as np
import cv2

# イメージ画像フォルダへのフルパス
image_path = "FULL_PATH"

### Read an image
# 読み込み処理 オプションを数字でも指定できる 0はグレイスケール
img = cv2.imread(image_path + 'messi5.jpg',0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()