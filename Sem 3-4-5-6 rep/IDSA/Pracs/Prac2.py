# Expt2 
# To perform enhancement and reduction of an image using Log and power transformations
import cv2
import numpy as np

img = cv2.imread('download.jpg')

# For Reduction log tranformation
# S=C * log (1+a)
# c = 255/(log(1 + max_input_pixel_value))
img_log = (np.log(img + 1) / (np.log(1 + np.max(img)))) * 255
img_log = np.array(img_log, dtype=np.uint8)

# For enhancement power transformation
# s = c*r^γ where c=225 Y=4.4
power_img = np.array(225 * (img / 225) ** 4.4, dtype='uint8')

# Display the image
cv2.imshow('log_image', img_log)
cv2.imshow('power_img', power_img)
cv2.imshow('original_img', img)
cv2.waitKey(0)
