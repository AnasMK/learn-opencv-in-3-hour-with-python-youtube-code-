import os
import cv2
import numpy as np

RESOURCES_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources')
WINDOW_NAME = 'Output'
kernal = np.ones((5,5), np.uint8)
img = cv2.imread(os.path.join(RESOURCES_FOLDER, 'bird.jpg'))
# img = cv2.resize(img, (300, 400))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)
# Edge detection
img_canny = cv2.Canny(img, 150, 200)

# image dialation: add edge thickness
img_dialation = cv2.dilate(img_canny, kernal, iterations=1)

# image erosion : make edge thinner
img_eroded = cv2.erode(img_dialation, kernal, iterations=1)

cv2.imshow('Gray Image', img_gray)
cv2.imshow('Blur Image', img_blur)
cv2.imshow('Edge Detected Image', img_canny)
cv2.imshow('Dialation Image', img_dialation)
cv2.imshow('Eroded Image', img_eroded)

cv2.waitKey(0)

