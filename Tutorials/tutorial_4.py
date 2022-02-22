import cv2
import numpy as np

img = np.zeros((600,800,3), np.uint8)

#畫線
cv2.line(img, (0,0), (300,400), (0,0,255), 1)                        #(畫在哪, 點1, 點2, color, 粗度)
cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,255), 2)    #畫對角線

#畫方形(可填滿)
cv2.rectangle(img, (300,0), (400, 100), (255,0,0), 1)
cv2.rectangle(img, (500,0), (600, 100), (255,0,0), cv2.FILLED)       #填滿

#畫圓形(可填滿)
cv2.circle(img, (300,400), 30, (100,0,150), 3)                       #(畫在哪, 圓心點, 半徑, color, 粗度)
cv2.circle(img, (300,500), 30, (0,100,150), cv2.FILLED)

#文字(putText 不支援中文)
cv2.putText(img, "Hello", (50,300), cv2.FONT_ITALIC, 1, (255,255,255), 1)    #(畫在哪, "內容", 文字框左下角位置, 字型, 字體大小, color, 粗度)

cv2.imshow("img", img)
cv2.waitKey(0)