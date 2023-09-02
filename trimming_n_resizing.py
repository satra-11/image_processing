import numpy as np
import cv2

img = cv2.imread("bird.jpg")
size = img.shape

# トリミング
my_img = img[: size[0]//2, : size[1] // 3]

# リサイズ。二倍にする。
my_img = cv2.resize(my_img, (my_img.shape[1] * 2, my_img.shape[0] * 2))

cv2.imshow("sample", my_img)

cv2.waitKey(0)
cv2.destroyAllWindows()