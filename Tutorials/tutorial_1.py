import cv2
#讀取圖片
img = cv2.imread("Media//Gumbo.jpg")
# img = cv2.resize(img, (300, 300))               #改變大小_1(x,y 像素)
img = cv2.resize(img, (0,0), fx = 2, fy = 2)    #改變大小_2(fx,fy 倍率)

cv2.imshow("Gumbo", img)   #(title, sorce)
cv2.waitKey(0)    #多久時間(ms)內等待按鍵 "q" 關閉，0 為永久


#讀取影片
cap = cv2.VideoCapture("Media//Cat.mp4")

while True:
  ret, frame = cap.read()    #回傳影片的下一禎是否取得成功及下一張的圖片
  if ret:
    frame = cv2.resize(frame, (0,0), fx = 0.2, fy = 0.2)
    cv2.imshow("Cat", frame)
  else:
    break
  if cv2.waitKey(1) == ord("q"):
    break

#讀取外接鏡頭
cap = cv2.VideoCapture(0)    #從編號 0 開始

while True:
  ret, frame = cap.read()    #回傳影片的下一禎是否取得成功及下一張的圖片
  if ret:
    frame = cv2.resize(frame, (0,0), fx = 1, fy = 1)
    cv2.imshow("pw310p", frame)
  else:
    break
  if cv2.waitKey(1) == ord("q"):
    break