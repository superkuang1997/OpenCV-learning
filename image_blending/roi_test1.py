import cv2
# Region of Interest  ROI
img = cv2.imread('../image/messi5.jpg')

# select the ball and copy it to another region in this image
ball = img[280:340, 330:390]

print(ball.shape)
print(img.shape)
img[273:333, 100:160] = ball
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
