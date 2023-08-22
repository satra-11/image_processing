import cv2

img = cv2.imread("bird.jpg")

cv2.imshow("sample", img)

# 関数キーが押されるまで、無期限待機
cv2.waitKey(0)
cv2.destroyAllWindows()
