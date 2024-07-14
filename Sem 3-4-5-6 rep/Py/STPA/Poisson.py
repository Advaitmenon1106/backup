import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
def poisson(avg, arr):
    newArr = np.zeros(len(arr))
    for i in range (0, len(arr)):
        newArr[i] = avg**arr[i]
    expo = np.exp(-avg)
    for x in range (0, len(arr)):
        newArr[x] = (newArr[x]*expo)/(math.factorial(arr[x]))
    return newArr

size = int(input("Enter a size: "))
origArr = np.arange(1, size)
average = int(input("Enter an average: "))
print (poisson(average, origArr))