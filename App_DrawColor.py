#R: 150 179 175 255 100 255
#G: 60 85 140 255 100 255
import cv2
import numpy as np


cap = cv2.VideoCapture(0)
ColorHSV = [[150, 179, 175, 255, 100, 255],    #Red
            [ 60,  85, 140, 255, 100, 255]]    #Green

ColorBGR = [[0, 0 ,255],
            [0, 255, 0]]

drawPoints = []    #[x, y, colorID]

#偵測顏色
def findcolor(img):
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  for i in range(len(ColorHSV)):
    lower = np.array([ColorHSV[i][0], ColorHSV[i][2], ColorHSV[i][4]])
    upper = np.array([ColorHSV[i][1], ColorHSV[i][3], ColorHSV[i][5]])
    filter = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask = filter)
    posx, posy = findcontours(filter)
    cv2.circle(imgContour, (posx, posy), 8, ColorBGR[i], cv2.FILLED)
    #紀錄行經的點位置(過濾雜訊)
    if posy != -1:
      drawPoints.append([posx, posy, i])  #i:colorID
  # cv2.imshow("result", result)

#偵測輪廓
def findcontours(img):
  contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
  x, y, wid, hei = -1, -1, -1, -1
  for cnt in contours:
    #畫輪廓
    # cv2.drawContours(imgContour, cnt, -1, (0, 0, 255), 3)
    area = cv2.contourArea(cnt)    #輪廓面積
    if area > 100:      
      peri = cv2.arcLength(cnt, True)                      #顯示輪廓長度
      vertices = cv2.approxPolyDP(cnt, peri*0.02, True)    #多邊形近似輪廓
      x, y, wid, hei = cv2.boundingRect(vertices)          #把圖形框起來
  return x+wid//2, y

def draw(drawpoints):
  for point in drawpoints:
    cv2.circle(imgContour, (point[0], point[1]), 8, ColorBGR[point[2]], cv2.FILLED)

while True:
  ret, frame = cap.read()
  if ret:
    frame = cv2.flip(frame, 1)    #鏡像翻轉(0:x軸翻轉、1:y軸翻轉)
    frame = cv2.resize(frame, (0,0), fx = 1.5, fy = 1.5)
    imgContour = frame.copy()
    cv2.imshow("pw310p", frame)
    findcolor(frame)
    draw(drawPoints)
    cv2.imshow("contour", imgContour)
  else:
    break
  if cv2.waitKey(1) == ord("q"):
    break