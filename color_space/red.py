import cv2
import numpy as np

img = cv2.imread('../image/seal1.jpg')
# COLOR_BGR2GRAY represents BGR → HSV
# H:0-180 S:0-255 V:0-255
redLower_1 = np.array([156, 43, 46])
redUpper_1 = np.array([179, 255, 255])

redLower_2 = np.array([0, 43, 46])
redUpper_2 = np.array([8, 255, 255])

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask1 = cv2.inRange(img_hsv, redLower_1, redUpper_1)
mask2 = cv2.inRange(img_hsv, redLower_2, redUpper_2)
mask = cv2.bitwise_or(mask1, mask2)

#cv2.imshow('img_hsv', img_hsv)
cv2.imshow('mask1', mask1)
cv2.imshow('mask2', mask2)
cv2.imshow('mask', mask)
cv2.waitKey(0)