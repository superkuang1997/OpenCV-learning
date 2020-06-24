import cv2
import numpy as np

img = cv2.imread('../image/messi5.jpg')
# 1.均值滤波
blur = cv2.blur(img, (3, 3))

# 上面的均值滤波也可以用方框滤波实现：normalize=True
# blur = cv2.boxFilter(img, -1, (3, 3), normalize=True)


# 2.高斯滤波
gau_blur = cv2.GaussianBlur(img, (3, 3), 0)

# 三张图片横向叠加对比显示
res = np.hstack((img, blur, gau_blur))
cv2.imshow('res', res)
cv2.waitKey(0)