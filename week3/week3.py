import cv2
import matplotlib.pyplot as plt

imgBGR = cv2.imread('lena.bmp')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
imgGray = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2GRAY)

plt.subplot(131), plt.imshow(imgBGR)
plt.subplot(132), plt.imshow(imgRGB)
plt.subplot(133), plt.imshow(imgGray, cmap='gray')
plt.show()