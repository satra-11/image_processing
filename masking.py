import cv2
import numpy as np

img = cv2.imread("bird.jpg")

mask = cv2.imread("assets/mask.png")

mask = cv2.resize(mask, (img.shape[1], img.shape[0]))

mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

my_img = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("sample", my_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
マスキングでは、白黒のチャンネル1の画像を用いる。
'''