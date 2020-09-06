import os
import cv2

RESOURCES_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources')
WINDOW_NAME = 'Output'

# To read video with opencv cv2.VideoCapture(file_path) need to be used
cap = cv2.VideoCapture(os.path.join(RESOURCES_FOLDER, 'waterfall.mp4'))

while True:
    success, img = cap.read()
    cv2.imshow(WINDOW_NAME, img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('Exit video!')
        break