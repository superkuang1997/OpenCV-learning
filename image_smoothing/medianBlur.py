import cv2

img = cv2.imread('salt_noise.bmp', 0)
# 均值滤波vs中值滤波
blur = cv2.blur(img, (5, 5))  # 均值滤波
median = cv2.medianBlur(img, 5)  # 中值滤波
