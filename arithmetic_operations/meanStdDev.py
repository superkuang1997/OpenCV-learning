import cv2

# 均值 & 方差（对比度）
img = cv2.imread('../image/img1.jpg', 1)
print(cv2.mean(img))
print(cv2.meanStdDev(img))
