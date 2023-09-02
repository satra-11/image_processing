import cv2
import numpy as np

img = cv2.imread("bird.jpg")

# アフィン変換に必要な行列を作る。
# 第一引数...回転の中心

mat = cv2.getRotationMatrix2D(tuple(np.array(img.shape[:2])/2), 180, 1.0)

# アフィン変換。
my_img = cv2.warpAffine(img, mat, img.shape[:2])

cv2.imshow("sample", my_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
このコードでは [:2] を使用して最初の2つの要素、つまり高さと幅の情報だけを取り出しています。
img の形状属性が (400, 600, 3) である場合、それぞれの要素は以下のように対応します：
img.shape[0] は高さを表すので、値は 400 です。
img.shape[1] は幅を表すので、値は 600 です。
img.shape[2] はチャンネル数を表すので、値は 3 です。
'''