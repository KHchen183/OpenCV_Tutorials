import cv2
import numpy as np

#色彩轉換
img = cv2.imread("Media//Gumbo.jpg")
img = cv2.resize(img, (0,0), fx = 1, fy = 1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("img", img)
cv2.imshow("Gumbo", gray)

#高斯模糊
blur = cv2.GaussianBlur(img, (15,15), 10)    #(source, 奇數的核, 標準差)
cv2.imshow("blur", blur)

#圖片邊緣
canny = cv2.Canny(img, 150, 200)             #(source, 最低門檻值, 最高門檻值)
cv2.imshow("canny", canny)

#圖片膨脹(線條變粗)
kernel = np.ones((3,3), np.uint8)
dilate = cv2.dilate(canny, kernel, iterations = 1)    #(source, 二微陣列的核, iterations:膨脹次數)
cv2.imshow("dilate", dilate)

#圖片侵蝕
kernel_1 = np.ones((3,3), np.uint8)
erode = cv2.erode(dilate, kernel_1, iterations = 1)
cv2.imshow("erode", erode)

cv2.waitKey(0)