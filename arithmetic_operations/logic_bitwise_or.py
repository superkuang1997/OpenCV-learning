import cv2

img1 = cv2.imread('../image/windowsLogo.jpg', 1)
img2 = cv2.imread('../image/LinuxLogo.jpg', 1)
dst = cv2.bitwise_or(img1, img2)
cv2.namedWindow('dst', cv2.WINDOW_AUTOSIZE)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('dst', dst)
k = cv2.waitKey(0)
cv2.destroyAllWindows()