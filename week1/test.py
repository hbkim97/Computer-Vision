import cv2

print("Hello OpenCV", cv2.__version__)

img = cv2.imread('lena.bmp')

cv2.imshow('my_image', img)
cv2.waitKey()
cv2.destroyAllWindows()
