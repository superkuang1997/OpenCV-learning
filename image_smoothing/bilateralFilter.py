import cv2

img = cv2.imread('../image/messi5.jpg')

# 双边滤波vs高斯滤波
gau = cv2.GaussianBlur(img, (5, 5), 0)  # 高斯滤波
blur = cv2.bilateralFilter(img, 9, 75, 75)  # 双边滤波
