import cv2
import numpy as np

img = cv2.imread('../image/messi5.jpg')
print(img.shape)
print(img.size)
print(img.dtype)
print(np.array(img))
