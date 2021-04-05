import cv2
import matplotlib.pyplot as plt

img_path = './lena.bmp' # 512x512x3

imgBGR = cv2.imread(img_path)
imgRGB = cv2.cvtColor(imgBGR, code = cv2.COLOR_BGR2RGB)
imgGray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

plt.imshow(imgGray, cmap='gray')
plt.show()