import cv2
import numpy as np

oldx = oldy = -1

def mouse_event(event, x, y, flags, param):
    global oldx, oldy

    if event  == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('EVNENT_LBUTTONDOWN: {},{}'.format(x,y))
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (255,0,0), 4, cv2.LINE_AA )
            cv2.imshow('img', img)
            oldx, oldy = x,y


img = np.full((500,500, 3), 255, dtype=np.uint8)

cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_event, img)

cv2.imshow('img', img)
cv2.waitKey()

cv2.destroyAllWindows()
