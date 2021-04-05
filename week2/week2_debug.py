import cv2
import matplotlib.pyplot as plt

img_path = 'lena.bmp' #512x512x3

imgBGR = cv2.imread(img_path)
imgRGB = cv2.cvtColor(imgBGR, cv2.IMREAD_GRAYSCALE)

plt.imshow(imgRGB)
plt.show()
print(0)