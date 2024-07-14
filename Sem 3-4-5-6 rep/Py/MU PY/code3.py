import numpy as np
x = np.array([2, 3, 4, 5, 6, 7, 8, 9])
print(x)
print(type(x))

x1 = np.array([[[2, 4],[4, 5]], [[7, 8], [6,7]]])
print (x1)

print (" ")

x1[-1][-1][-1] = 9
print (x1)

print (" ")

x3 = np.array([[[2, 3], [4, 5]], [[7,8], [6, 7]]])
print (x3)

avg = (x3[:, :, 0] + x3[:, :, 1])/2

print (avg)
