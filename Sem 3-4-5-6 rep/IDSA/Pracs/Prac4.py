# To perform thresholding and histogram equalization
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('download.jpg', 0)

# Histogram
hist, bins = np.histogram(img.flatten(), 256, [0, 256])
plt.hist(img.flatten(), 256, [0, 256])
plt.xlim([0, 256])
plt.show()

# Thresholding
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary", thresh)
cv2.waitKey()

# Histogram Equilization
equ = cv2.equalizeHist(img)
cv2.imshow("res", equ)
cv2.waitKey()
