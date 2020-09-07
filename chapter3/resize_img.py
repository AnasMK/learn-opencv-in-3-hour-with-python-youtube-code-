import os
import cv2

RESOURCES_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources')

img = cv2.imread(os.path.join(RESOURCES_FOLDER, 'anas2.jpeg'))

print(img.shape)

img_resize = cv2.resize(img, (300, 400))


cv2.imshow('Resize Image', img_resize)
cv2.waitKey(0)