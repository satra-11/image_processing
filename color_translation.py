import cv2
import numpy as np

img = cv2.imread("bird.jpg")

my_img = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)

# LAB色空間に変換。色の評価や比較がしやすくなるそう。
cv2.imshow("sample", my_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
