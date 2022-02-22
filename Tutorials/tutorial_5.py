import cv2
import numpy as np

#偵測顏色
#HSV 的色彩空間表示 (Hue:色調值、Saturation:飽和度、Value:亮度)

img = cv2.imread("Media//SpongeBob.jpg")
img = cv2.resize(img, (0,0), fx = 1, fy = 1)

#建立動態控制條
cv2.namedWindow("TrackBar")               #建立視窗
cv2.resizeWindow("TrackBar", 640, 320)    #調整視窗大小
#建立控制條
def empty(v):    #會傳入一個變數
  pass
cv2.createTrackbar("Hue Min", "TrackBar", 0, 179, empty)    #("Name", 放在哪, 最小值, 最大值, 控制條改變後執行的函式)  
cv2.createTrackbar("Hue Max", "TrackBar", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBar", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBar", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBar", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBar", 255, 255, empty)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
while True:
  h_min = cv2.getTrackbarPos("Hue Min", "TrackBar")    #取得控制條的值(控制條名稱, 視窗名稱)
  h_max = cv2.getTrackbarPos("Hue Max", "TrackBar")
  s_min = cv2.getTrackbarPos("Sat Min", "TrackBar")
  s_max = cv2.getTrackbarPos("Sat Max", "TrackBar")
  v_min = cv2.getTrackbarPos("Val Min", "TrackBar")
  v_max = cv2.getTrackbarPos("Val Max", "TrackBar")
  print(h_min, h_max, s_min, s_max, v_min, v_max)

  #過濾顏色
  lower = np.array([h_min, s_min, v_min])
  upper = np.array([h_max, s_max, v_max])
  filter = cv2.inRange(hsv, lower, upper)    #(lower:HSV min, upper:HSV max) 所以要用 array 表示
  #過濾出實際顏色
  result = cv2.bitwise_and(img, img, mask = filter)    #bitwise_and 函式是對兩張圖做 "AND" 運算，最後在用 mask 過濾
                                                       #因為這裡只有一張圖(所以 img AND img 結果不變，直接用 mask 過濾)

  cv2.imshow("img", img)
  cv2.imshow("hsv", hsv)
  cv2.imshow("filter", filter)
  cv2.imshow("result", result)
  cv2.waitKey(100)