import numpy as np
import cv2
import os

""""
遍历roi文件夹中的所有文件，消除黑色字迹后保存到output
"""

def remove_handwritting(filename):
    Lower = np.array([0, 0, 120])
    Upper = np.array([180, 255, 255])
    row_img = cv2.imread('../image/input/' + str(filename))
    img = cv2.imread('../image/roi/' + str(filename))
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img_hsv, Lower, Upper)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    average = cv2.mean(row_img)[:3]
    for row in range(mask.shape[0]):
            for col in range(mask.shape[1]):
                if all(mask[row, col] == [0, 0, 0]):
                    img[row, col] = average

    #cv2.imshow('img', img)
    if not os.path.exists('../image/output'):
        os.mkdir('../image/output')
    cv2.imwrite('../image/output/' + filename, img)
    #cv2.waitKey(0)

for file in os.listdir('../image/roi/'):
    remove_handwritting(file)