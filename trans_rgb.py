import cv2
from matplotlib import pyplot as plt

img = cv2.imread('image/img1.jpg',1)
b, g, r = cv2.split(img)
trans_img = cv2.merge([r,g,b])
plt.imshow(trans_img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
