import cv2

img = cv2.imread('../image/windowsLogo.jpg', 1)
dst = cv2.bitwise_not(img)
cv2.namedWindow('dst', cv2.WINDOW_AUTOSIZE)
cv2.imshow('img', img)
cv2.imshow('dst', dst)
k = cv2.waitKey(0)
cv2.destroyAllWindows()