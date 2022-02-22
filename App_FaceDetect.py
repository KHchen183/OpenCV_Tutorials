import cv2

#讀取外接鏡頭
cap = cv2.VideoCapture(0)    #從編號 0 開始

while True:
  ret, frame = cap.read()    #回傳影片的下一禎是否取得成功及下一張的圖片
  if ret:
    frame = cv2.resize(frame, (0,0), fx = 1.5, fy = 1.5)
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faceCascade = cv2.CascadeClassifier("Tutorials//face_detect.xml")    #人臉模型
    faceRect = faceCascade.detectMultiScale(grayframe, 1.5, 5)           #回傳矩形框
    for (x, y, wid, hei) in faceRect:
      cv2.rectangle(frame, (x, y), (x+wid, y+hei), (0, 255, 0), 2)

    cv2.imshow("pw310p", frame)
    # cv2.imshow("grayframe", grayframe)
  else:
    break
  if cv2.waitKey(1) == ord("q"):
    break