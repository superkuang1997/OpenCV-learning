import cv2
# Region of Interest  ROI
img = cv2.imread('../image/messi5.jpg')
ball = img[280:340, 330:390]
gray = cv2.cvtColor(ball, cv2.COLOR_BGR2GRAY)
gray_ball = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
img[280:340, 330:390] = gray_ball
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()