import cv2
import numpy as np

img = cv2.imread('../image/img1.jpg', 0)

# 阈值分割  ret = current threshold
ret, th = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
cv2.imshow('thresh', th)
cv2.waitKey(0)