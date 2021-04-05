import cv2
import numpy as np

hansung1 = cv2.VideoCapture('C:/Users/gusqo/[1]vision/week3/hansung.mp4')
hansung2 = cv2.VideoCapture('video1.mp4')

if not hansung2.isOpened():
    print('[!] video open failed!')

w2 = int(hansung2.get(cv2.CAP_PROP_FRAME_WIDTH))
h2 = int(hansung2.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps2 = hansung2.get(cv2.CAP_PROP_FPS) #자연스럽지않으면 수정
fourcc2 = cv2.VideoWriter_fourcc(*'DIVX')

w1 = int(hansung1.get(cv2.CAP_PROP_FRAME_WIDTH))
h1 = int(hansung1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps1 = hansung1.get(cv2.CAP_PROP_FPS) #자연스럽지않으면 수정
fourcc1 = cv2.VideoWriter_fourcc(*'DIVX')

square = np.zeros((h1, w1, 3), np.uint8)
square[:] = (0, 0, 0)

roi = 960, 0, 320, 240

image = cv2.rectangle(square, roi, (255,255,255), cv2.FILLED)


while True :
    ret2, frame2 = hansung2.read()
    if not ret2 :
        break

    re_frame2 = cv2.resize(frame2, (320, 240),) #resize


    cv2.imshow('re_hansung2', re_frame2)
    #cv2.imshow('add', frame_add)

    if cv2.waitKey(30) == 27:
        break

hansung2.release()
cv2.destroyAllWindows()