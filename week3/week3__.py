import cv2

cap = cv2.VideoCapture('./hansung.mp4')

h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
n_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)

print(h, w, n_frame, fps)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('./bbb.avi', fourcc, fps, (w, h))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_inv = ~frame #50 -> 255-50 = 205
    cv2.imshow('frame_inv', frame_inv)
    cv2.imshow('frame', frame)

    if cv2.waitKey(30)==27:
        break

    #out.write(frame_inv)

# out.release()
cap.release()
cv2.destroyAllWindows()