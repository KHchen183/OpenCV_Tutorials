import cv2
import numpy as np
import random as rd

#創建隨機圖片
#OpenCV 的 RGB 順序為 [B,G,R]

img = np.empty((300, 300, 3), np.uint8)    #uint8:正整數 0 ~ 255
for row in range(300):
  for col in range(300):
    # img[row][col] = [255, 0, 0]
    img[row][col] = [rd.randint(0,255), rd.randint(0,255), rd.randint(0,255)]


cv2.imshow("Gumbo", img)

#切割圖片(坐標系)
Img = cv2.imread("Media//Gumbo.jpg")

newImg_1 = Img[:200, :200]    #座標從圖片左上角開始算，向右x、向下y
newImg_2 = Img[:200, 200:400]

cv2.imshow("Img", Img)
cv2.imshow("newImg_1", newImg_1)
cv2.imshow("newImg_2", newImg_2)
cv2.waitKey(0)
