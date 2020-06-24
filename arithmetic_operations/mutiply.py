import cv2
# 0乘任何数为0，得到黑色区域
# 由于图像边缘反锯齿，所以部分像素不为0
img1 = cv2.imread('../image/windowsLogo.jpg', 1)
img2 = cv2.imread('../image/LinuxLogo.jpg', 1)
dst1 = cv2.multiply(img1, img2)
cv2.imshow('dst1', dst1)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
