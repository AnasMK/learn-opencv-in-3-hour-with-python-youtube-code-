import os
import cv2

RESOURCES_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources')

img = cv2.imread(os.path.join(RESOURCES_FOLDER, 'anas2.jpeg'))
img = cv2.resize(img, (300, 400))

print('Image shape: ', img.shape)

img_cropped = img[75:270,90:235]

print('Cropped Image Shape: ', img_cropped.shape)

cv2.imshow('Output Image',img)
cv2.imshow('Cropped Image', img_cropped)
cv2.waitKey(0)