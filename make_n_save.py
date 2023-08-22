import numpy as np
import cv2

# 画像サイズの決定
img_size = (512, 512)

'''
画像の情報を持つデータ列の作成。つまり、各要素が[0,0,255]の512×512の行列を作る。
・内包表記の多重ループ。
    new_list = [expression for item in iterable if condition]
    が型なので、まず一回ループを回して、それを要素としてもう一回ループを回す。
・[0,0,255]なので真っ赤。
・各要素は0~255の値しか取らないので、dtypeを指定。
・画像が転置されることに注意？
'''
my_img = np.array(
    [
        [
            [0, 0, 255] for _ in range(img_size[1])
        ] for _ in range(img_size[0])
    ], dtype="uint8")

# 出力
cv2.imshow("sample", my_img)

# 関数キーが押されるまで、無期限待機
cv2.waitKey(0)
cv2.destroyAllWindows()

# 画像の生成
cv2.imwrite("my_red_img.jpg", my_img)


