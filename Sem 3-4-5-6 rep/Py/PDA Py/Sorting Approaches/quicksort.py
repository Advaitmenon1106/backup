import numpy as np
import random as rand
n = 20
array1 = []
for x in range (0, n):
    elements = rand.randint(0, 100)
    array1.append(elements)

def partition(arr, l, h):
    le = len(arr)
    pivot = arr[h]
    i = l
    j = l
    while j<h:
        if arr[j] < pivot:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i+=1
        j+=1
    temp1 = arr[i]
    arr[l] = arr[i]
    arr[i] = temp1
    return arr

a2 = partition(array1, array1[0], array1[n-2])
print (a2)



def sort():
    pass