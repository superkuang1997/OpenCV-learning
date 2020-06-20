import cv2

img1 = cv2.imread('../image/messi5.jpg')
img2 = cv2.imread('../image/img1.jpg')

img1 = img1[0:300,0:300]
img2 = img2[0:300,0:300]
dst = cv2.addWeighted(img1,0.5,img2,0.5,0)
cv2.imshow('dst',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()