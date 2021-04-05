import cv2
import numpy as np

hansung1 = cv2.VideoCapture('C:/Users/gusqo/[1]vision/week3/hansung.mp4')

w1 = int(hansung1.get(cv2.CAP_PROP_FRAME_WIDTH))
h1 = int(hansung1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps1 = hansung1.get(cv2.CAP_PROP_FPS) #자연스럽지않으면 수정
fourcc1 = cv2.VideoWriter_fourcc(*'DIVX')

square = np.zeros((h1, w1, 3), np.uint8)
square[:] = (255, 255, 255)

roi = 960, 0, 320, 240

cv2.rectangle(square, roi, (0, 0, 0), cv2.FILLED)

cv2.imshow('Rectangle', square)
cv2.waitKey()
cv2.destroyAllWindows()