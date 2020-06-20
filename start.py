import cv2

print(cv2.__version__)
img = cv2.imread('image/img1.jpg', 1)
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image', img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
