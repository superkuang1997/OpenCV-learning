import cv2

img = cv2.imread('../image/img1.jpg')
# COLOR_BGR2GRAY represents BGR → Gray
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)

cv2.imshow('img', img)
cv2.imshow('gray', img_gray)
cv2.waitKey(0)