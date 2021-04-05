import cv2

# 파일을 불러온다.
cap = cv2.VideoCapture('./resource/video1.mp4')
vi2 = cv2.VideoCapture('./resource/hansung.mp4')

# 오류를 처리한다.
if not cap.isOpened() or not vi2.isOpened():
    print('[!] video open failed!')

# 영상 정보의 값을 변수에 저장한다.
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
n_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)

h2 = vi2.get(cv2.CAP_PROP_FRAME_HEIGHT)
w2 = vi2.get(cv2.CAP_PROP_FRAME_WIDTH)
n_frame2 = vi2.get(cv2.CAP_PROP_FRAME_COUNT)
fps2 = vi2.get(cv2.CAP_PROP_FPS)

delay = int(1000/fps)

# 시작 프레임을 0으로 설정한다.
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
vi2.set(cv2.CAP_PROP_POS_FRAMES, 0)

print(h, w, n_frame, fps)
print(h2, w2, n_frame2, fps2)

# 원숭이 영상을 오른쪽 위에서 합성한다.
x_offset = 950
y_offset = 10

# 합성한 영상을 저장하기 위한 코드.
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('./output_inv.avi',fourcc,fps,(int(w2),int(h2)))

while True:
    ret, frame = cap.read()
    ret2, frame2 = vi2.read()
    if not ret:
        break

    # 원숭이 영상의 크기를 줄인다.
    frame = cv2.resize(frame, dsize=(320, 240), interpolation=cv2.INTER_AREA)

    # 영상을 합성한다. (이미지 단위로 합성)
    frame2[y_offset:y_offset + frame.shape[0], x_offset:x_offset + frame.shape[1]] = frame

    # 합성된 영상을 프레임 단위로 저장한다.
    out.write(frame2)

    # 합성된 영상을 재생한다.
    cv2.imshow('frame2', frame2)

    if cv2.waitKey(delay) == 27:
        break

cap.release()
vi2.release()
out.release()
cv2.destroyAllWindows()