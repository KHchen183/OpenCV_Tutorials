import cv2
import numpy as np

#讀取外接鏡頭
cap = cv2.VideoCapture(0)

#建立動態控制條
cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar", 640, 320)
def empty(v):
  pass
cv2.createTrackbar("Hue Min", "TrackBar", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBar", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBar", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBar", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBar", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBar", 255, 255, empty)

while True:
  h_min = cv2.getTrackbarPos("Hue Min", "TrackBar")
  h_max = cv2.getTrackbarPos("Hue Max", "TrackBar")
  s_min = cv2.getTrackbarPos("Sat Min", "TrackBar")
  s_max = cv2.getTrackbarPos("Sat Max", "TrackBar")
  v_min = cv2.getTrackbarPos("Val Min", "TrackBar")
  v_max = cv2.getTrackbarPos("Val Max", "TrackBar")
  print(h_min, h_max, s_min, s_max, v_min, v_max)

  #讀取鏡頭每一禎的畫面
  ret, frame = cap.read()
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  #過濾顏色
  lower = np.array([h_min, s_min, v_min])
  upper = np.array([h_max, s_max, v_max])
  filter = cv2.inRange(hsv, lower, upper)

  #過濾出實際顏色
  result = cv2.bitwise_and(frame, frame, mask = filter)

  #顯示
  cv2.imshow("pw310p", frame)
  # cv2.imshow("hsv", hsv)
  cv2.imshow("filter", filter)
  cv2.imshow("result", result)
  cv2.waitKey(100)
