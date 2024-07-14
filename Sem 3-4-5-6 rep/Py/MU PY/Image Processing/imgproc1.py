import numpy as np
from matplotlib import pyplot as plt
img = plt.imread("redthing.jpg")
print (img)
plt.imshow(img)
plt.show()
x = [110, 200]
y = [10, 156]
# plt.plot(x, y, color="red") #draws a RED line from (110, 10) to (200, 156)
img2 = img[:, :, 0]
plt.imshow(img2)
plt.show()
print ("")
print ("")
print (img2)
red = img[399:682, 406:651, :]
plt.imshow(red)
plt.show()
#test1 = red[:, :, 2]
#plt.imshow(test1)
#plt.show()