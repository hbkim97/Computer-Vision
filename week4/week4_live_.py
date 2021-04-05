import cv2
import numpy as np

def onChange(k):
    array = np.full(img.shape, k , dtype=np.uint8)
    dst = cv2.add(img, array)
    cv2.imshow('img', dst)

img = cv2.imread('C:/Users/gusqo/[1]vision/week1/lena.bmp')

cv2.imshow('img',img)

cv2.createTrackbar('brightness', 'img', 0, 100, onChange)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()

