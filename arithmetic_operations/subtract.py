import cv2
# dst1：img1中颜色值减去255直接为0，颜色为黑色
# dst2：255减去img1中的颜色值，可以得到不同的颜色值,颜色为彩色
img1 = cv2.imread('../image/windowsLogo.jpg', 1)
img2 = cv2.imread('../image/LinuxLogo.jpg', 1)
dst1 = cv2.subtract(img1, img2)
dst2 = cv2.subtract(img2, img1)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
