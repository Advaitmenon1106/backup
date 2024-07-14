# Expt3 
# To perform bit wise slicing of the pixels of an image
import cv2
import numpy as np

img = cv2.imread('download.jpg', 0)

out = []

for k in range(0, 7):
    plane = np.full((img.shape[0], img.shape[1]), 2 ** k, np.uint8)
    res = cv2.bitwise_and(plane, img)
    x = res * 255
    out.append(x)

cv2.imshow("bit plane", np.hstack(out))
cv2.waitKey()
