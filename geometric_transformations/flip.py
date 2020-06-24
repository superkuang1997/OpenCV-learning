import cv2

img = cv2.imread('../image/img1.jpg', 0)
dst1 = cv2.flip(img, 0)  # 垂直翻转
dst2 = cv2.flip(img, 1)  # 水平翻转
dst3 = cv2.flip(img, -1)  # 水平垂直翻转

cv2.imshow('img1', dst1)
cv2.imshow('img2', dst2)
cv2.imshow('img3', dst3)
cv2.waitKey(0)