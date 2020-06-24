import cv2
# 0表示黑色，0加上任何数仍然是0，故颜色没有变化
# 255表示白色，255加上任何数仍然是255，故颜色是白色
img1 = cv2.imread('../image/windowsLogo.jpg', 1)
img2 = cv2.imread('../image/LinuxLogo.jpg', 1)
dst = cv2.add(img1, img2)
cv2.namedWindow('dst', cv2.WINDOW_AUTOSIZE)
cv2.imshow('dst', dst)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
