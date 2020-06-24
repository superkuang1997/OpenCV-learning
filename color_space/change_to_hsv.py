import cv2
import numpy as np

img = cv2.imread('../image/seal3.jpg')
# COLOR_BGR2GRAY represents BGR → HSV
# H:0-180 S:0-255 V:0-255
redLower = np.array([156, 43, 46])
redUpper = np.array([179, 255, 255])
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(img_hsv, redLower, redUpper)

cv2.imshow('img_hsv', img_hsv)
cv2.imshow('mask', mask)
cv2.waitKey(0)