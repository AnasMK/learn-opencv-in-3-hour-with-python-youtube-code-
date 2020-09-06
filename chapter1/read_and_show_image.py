import os
import cv2

print('OpenCV Package Imported!')

RESOURCES_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources')
print(os.path.join(RESOURCES_FOLDER, 'anas.jpeg'))
# Read image file
img = cv2.imread(os.path.join(RESOURCES_FOLDER, 'anas.jpeg'))

# show image
WINDOW_NAME = 'Output'
cv2.imshow(WINDOW_NAME, img)

# cv2.imshow show and close image immediately
# needs cv2.waitKey()
# cv2.waitKey(0) infinite delay until key pressed
# cv2.waitKey(1) 1ms delay
# cv2.waitKey(1000) 1s delay
cv2.waitKey(0)
