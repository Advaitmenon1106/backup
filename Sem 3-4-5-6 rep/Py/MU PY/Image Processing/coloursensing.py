import numpy as np
from matplotlib import pyplot as plt

rainbow = plt.imread("Rainbow2.png")
plt.imshow(rainbow)
plt.show()
red = rainbow[98:99, 17:20]
plt.imshow(red)
plt.show()
print (red)