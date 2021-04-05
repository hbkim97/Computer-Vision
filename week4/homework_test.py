# 'hansung.mp4' 열기, 'video1.mp4' 열기, 동시에 한 영상으로 출력하기
import cv2
import numpy as np

#동영상 불러오기
hansung1 = cv2.VideoCapture('C:/Users/gusqo/[1]vision/week3/hansung.mp4')
hansung2 = cv2.VideoCapture('video1.mp4')
if not hansung1.isOpened():
    print('[!] video open failed!')

w1 = int(hansung1.get(cv2.CAP_PROP_FRAME_WIDTH))
h1 = int(hansung1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps1 = hansung1.get(cv2.CAP_PROP_FPS)
fourcc1 = cv2.VideoWriter_fourcc(*'DIVX')

if not hansung2.isOpened():
    print('[!] video open failed!')

w2 = int(hansung2.get(cv2.CAP_PROP_FRAME_WIDTH))
h2 = int(hansung2.get(cv2.CAP_PROP_FRAME_HEIGHT))
''' 
fps2 = hansung2.get(cv2.CAP_PROP_FPS)
fourcc2 = cv2.VideoWriter_fourcc(*'DIVX')
'''

# 도화지 만들기
square = np.zeros((h1, w1, 3), np.uint8) #첫번째 동영상 크기에 맞는 도화지 생성
square[:] = (0, 0, 0) #색 : 검정

roi = 960, 0, 320, 240 #두번째 동영상이 들어갈 위치 선정

cv2.rectangle(square, roi, (255, 255, 255), cv2.FILLED) #두번째 영상이 삽입될 부분 / 색: 하양

out = cv2.VideoWriter('./1632021김현배.avi', fourcc1, fps1, (w1, h1))

while True:
    ret1, frame1 = hansung1.read()
    if not ret1: #ret = false 인 경우
        break

    ret2, frame2 = hansung2.read()
    ''' 첫번째 영상의 길이에 맞출때 두번째 영상을 반복시킨다.
    if(hansung2.get(cv2.CAP_PROP_POS_FRAMES) == hansung2.get(cv2.CAP_PROP_FRAME_COUNT)):
        hansung2.open('video1.mp4')'''

    if not ret2:
        break

    # 두번째 동영상 resize
    resize = cv2.resize(frame2, (320, 240))  # resize
    # square(도화지)에 더할때 우측 상단은 검정색(0,0,0)으로 남아있어야함.
    # 두번째 동영상이 들어갈 위치는 saturate로 인해 0 아래로 내려가지 않음
    frame_add = cv2.subtract(frame1, square)

    # 두번째 영상이 들어갈 위치 잡아주기
    roi_ = frame_add[0:240, w1 - 320:w1]
    # roi_ + 두번째 영상
    roi_add = cv2.add(roi_, resize)

    #roi에 roi_add영상 추가
    np.copyto(roi_, roi_add)

    cv2.imshow('frame_add', frame_add) # square + 1번 동영상 결과

    out.write(frame_add) #출력

    if cv2.waitKey(30) == 27: # 키 입력 대기 시간 : 30ms / esc의 아스키 : 27
        break

hansung1.release()
hansung2.release()
out.release()
cv2.destroyAllWindows()