import cv2

src = cv2.imread('candies.png')
print(src.shape)

b,g,r = cv2.split(src)

b[:, :] = 0

list_bgr = [b,g,r]

rec = cv2.merge(list_bgr)

print(b.shape)

cv2.imshow('src', src)
#cv2.imshow('b', b)
#cv2.imshow('g', g)
#cv2.imshow('r', r)
cv2.imshow('rec', rec)

cv2.waitKey()
cv2.destroyAllWindows()