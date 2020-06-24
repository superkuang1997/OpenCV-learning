import cv2
# 除法一般会得到一个较小的值，故黑色区域较大
img1 = cv2.imread('../image/windowsLogo.jpg', 1)
img2 = cv2.imread('../image/LinuxLogo.jpg', 1)
dst1 = cv2.divide(img1, img2)
dst2 = cv2.divide(img2, img1)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
