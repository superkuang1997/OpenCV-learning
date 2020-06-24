import cv2

img = cv2.imread('../image/img1.jpg')

# 按照指定的宽度、高度缩放图片
res = cv2.resize(img, (400, 300))
# 按照比例缩放，如x,y轴均放大一倍
res2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

cv2.imshow('shrink', res)
cv2.imshow('zoom', res2)
cv2.waitKey(0)