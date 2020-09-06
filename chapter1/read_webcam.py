import os
import cv2

WINDOW_NAME = 'Output'

# To read video with opencv cv2.VideoCapture(device_num) need to be used
cap = cv2.VideoCapture(0)
cap.set(3, 640) # set width
cap.set(4, 480) # set height

while True:
    success, img = cap.read()
    cv2.imshow(WINDOW_NAME, img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('Exit webcam!')
        break