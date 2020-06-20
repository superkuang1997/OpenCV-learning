import cv2

img = cv2.imread('../image/messi5.jpg')

b, g, r = cv2.split(img)
b = img[:,:,0] # set all blue pixel to zero
img = cv2.merge((g, b, r))

img[:,:,2] = 0  # set all red pixel to zero, this is a better way

cv2.imshow('image', img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()