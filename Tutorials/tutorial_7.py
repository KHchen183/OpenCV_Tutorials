import cv2

#人臉辨識
img = cv2.imread("Media//Lisa.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier("Tutorials//face_detect.xml")    #載入已經被訓練過的人臉模型
faceRect = faceCascade.detectMultiScale(gray, 1.1, 5)     #(source, 圖片縮小的倍率, 至少被偵測幾次)，回傳矩形的框

for (x, y, wid, hei) in faceRect:
  cv2.rectangle(img, (x, y), (x+wid, y+hei), (0, 255, 0), 2)

cv2.imshow("img", img)
cv2.imshow("gray", gray)
cv2.waitKey(0)