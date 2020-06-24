import cv2
import numpy as np

def track_back(x):
    pass

img = cv2.imread('../image/seal9.jpg')
img = cv2.resize(img, (800, 600))
cv2.namedWindow('window',cv2.WINDOW_AUTOSIZE)
# COLOR_BGR2GRAY represents BGR → HSV
# H:0-180 S:0-255 V:0-255
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.createTrackbar('h_high', 'window', 15, 180, track_back)
cv2.createTrackbar('s_high', 'window', 255, 255, track_back)
cv2.createTrackbar('v_high', 'window', 255, 255, track_back)
cv2.createTrackbar('h_low', 'window', 0, 180, track_back)
cv2.createTrackbar('s_low', 'window', 40, 255, track_back)
cv2.createTrackbar('v_low', 'window', 50, 255, track_back)



while True:

    h_high = cv2.getTrackbarPos('h_high', 'window')
    s_high = cv2.getTrackbarPos('s_high', 'window')
    v_high = cv2.getTrackbarPos('v_high', 'window')
    h_low = cv2.getTrackbarPos('h_low', 'window')
    s_low = cv2.getTrackbarPos('s_low', 'window')
    v_low = cv2.getTrackbarPos('v_low', 'window')

    Lower = np.array([h_low, s_low, v_low])
    Upper = np.array([h_high, s_high, v_high])


    mask = cv2.inRange(img_hsv, Lower, Upper)

    cv2.imshow('window', mask)

    if cv2.waitKey(30) == 27:
        break