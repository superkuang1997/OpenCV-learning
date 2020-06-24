import cv2
import numpy as np

def adjust_contrast_brightness(image, c, b):
    """
    adjust_contrast_brightness(image, c, b) -> dst
    :param image: img 8-bit 3-channel image
    :param c: float, contrast
    :param b: float, brightness
    :return: dst
    """

    h, w, ch = image.shape
    blank = np.zeros([h, w, ch], dtype=image.dtype)
    dst = cv2.addWeighted(image, c, blank, 1-c, b)
    return dst

img = cv2.imread('../image/img1.jpg')
dst = adjust_contrast_brightness(img, 1.5, 50)
cv2.imshow('img', dst)
k = cv2.waitKey(0)
cv2.destroyAllWindows()