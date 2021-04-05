import cv2
import numpy as np

img = np.zeros((500,500), dtype=np.uint8)

def onChange(pos):
    value = pos
    img[:] = value
    cv2.imshow('img', img)

cv2.namedWindow('img')
cv2.createTrackbar('brightness', 'img', 0, 255, onChange)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()