import cv2

img = cv2.imread("bird.jpg")

retval , my_img = cv2.threshold(img,200, 255, cv2.THRESH_TOZERO)
cv2.imshow("sample", my_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
    画像容量を小さくするための、閾値処理。
    THRESH_TOZEROでは閾値を超えるピクセルは変更されず、それ以外のピクセルは0(黒)になる。
'''