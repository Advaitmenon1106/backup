import numpy as np
size = int(input ("Enter the size of array: "))
arr = np.empty(shape=size, dtype=int)
import random as rand
import time as t

for i in range (0, size):
    #element = int(input("Enter an element: "))
    element = rand.randint(0, 100)
    arr[i] = element

print ("Unsorted: ", arr)

arr = np.sort(arr, kind='quicksort')

print ("Sorted: ", arr)

search = int(input("Search an element: "))

mid = (size-1)//2
low = 0
high = size-1


while low<=high:
    mid = (low+high)//2
    if search == arr[mid]:
        print("Position of ", search, " : ", mid)
        break
    elif arr[mid] < search:
        low = mid+1
    elif arr[mid] > search:
        high = mid-1