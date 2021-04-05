# 키보드 이벤트

import cv2

img = cv2.imread('C:/Users/gusqo/[1]vision/week1/lena.bmp', cv2.IMREAD_GRAYSCALE)

cv2.imshow('img', img)

while True:
    key= cv2.waitKey()
    if key == ord('i') or key == ord('I'):
        img = ~img
        cv2.imshow('img', img)
    elif key == 27:
        break

cv2.destroyAllWindows()