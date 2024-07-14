import random
import math

No_Iter = 1000000000
counter = 0
for i in range(0, No_Iter):
    x = random.random()
    y = random.random()
    if x**2 + y**2 < 1:
        counter += 1

print('Value of PI: ', counter*4/No_Iter, 'actual value of PI: ', math.pi)