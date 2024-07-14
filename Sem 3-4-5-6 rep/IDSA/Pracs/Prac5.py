# Expt5 
# To study and obtain the output for averaging filter and median filter

import cv2
import numpy as np

img = cv2.imread('download.jpg', 0)

# Averaging Filter
kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernel)
cv2.imshow("Averaging", dst)
cv2.waitKey()

# Median Filter
median = cv2.medianBlur(img, 5)
cv2.imshow("Median", median)
cv2.waitKey()
