
#       =================== SETTINGS YOUR VIDEO_CAPTURED WEBCAM ================

#      Setting kích thước khung hình 

import cv2
cap = cv2.VideoCapture(0)
#   Xuât kích thước khung hình mặc định
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#   Setting lại kích thước khung hình
#   SYNTAX: cap.set(par_1, par_2)   par_1: Index đại diện cho chiều dài (WIDTH) khung ảnh, par_2: kích thước mới của khung ảnh muốn setting lại 
cap.set(3,640)     #   Width of the image      MAX of width is 1280 pixels
cap.set(4,360)      #   Height of the image     MAX of height is 720 pixels

#   Xuất ra kích thước khung hình mới
print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Picture", frame)
    if cv2.waitKey(10) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
 