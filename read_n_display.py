import cv2

img = cv2.imread("bird.jpg")

cv2.imshow("sample", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
