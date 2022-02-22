import cv2

img = cv2.imread("Media//shape.jpg")
imgcopy = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(img, 150, 200)    #偵測邊緣

#偵測輪廓
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
                                      #(source, mode, method)
                                      # mode:外輪廓、內倫擴、內外都要，method:壓縮垂直的輪廓點

for cnt in contours:
  #畫輪廓
  cv2.drawContours(imgcopy, cnt, -1, (255,0,0), 3,)    #(image, contours, contourIdx:要繪製的輪廓序號，-1 代表所有, color, thickness)
  #顯示輪廓面積
  area = cv2.contourArea(cnt)        #若值為"0.0"的可能是雜訊點
  # print(area)
  if area > 100:      
    #顯示輪廓長度
    peri = cv2.arcLength(cnt, True)    #(curve, closed:是否為閉合)
    # print(peri)
    #多邊形近似輪廓
    vertices = cv2.approxPolyDP(cnt, peri*0.02, True)    #(curve, epsilon:近似值, closed)，回傳近似的多邊形的頂點位置
    corners = len(vertices)    #頂點數目
    #把圖形框起來
    x, y, wid, hei = cv2.boundingRect(vertices)
    cv2.rectangle(imgcopy, (x,y), (x+wid, y+hei), (0, 0, 255), 2)
    #判斷多邊形
    if corners == 3:
      cv2.putText(imgcopy, "triangle", (x,y-5), cv2.FONT_ITALIC, 0.7, (255, 0, 0), 2)
    elif corners == 4:
      cv2.putText(imgcopy, "rectangle", (x,y-5), cv2.FONT_ITALIC, 0.7, (255, 0, 0), 2)
    elif corners == 5:
      cv2.putText(imgcopy, "pantagon", (x,y-5), cv2.FONT_ITALIC, 0.7, (255, 0, 0), 2)
    elif corners >= 6:
      cv2.putText(imgcopy, "circle", (x,y-5), cv2.FONT_ITALIC, 0.7, (255, 0, 0), 2)

cv2.imshow("img", img)
cv2.imshow("canny", canny)
cv2.imshow("imgcopy", imgcopy)
cv2.waitKey(0)