import cv2

cap = cv2.VideoCapture('hansung.mp4')

h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
n_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)

fps = cap.get(cv2.CAP_PROP_FPS)

print(h, w, n_frame, fps)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    edge = cv2.Canny(frame, 50, 150)
    cv2.imshow('edge', edge)
    cv2.imshow('frame', frame)

    if cv2.waitKey(30)==27:
        break

cap.release()
cv2.destroyAllWindows()