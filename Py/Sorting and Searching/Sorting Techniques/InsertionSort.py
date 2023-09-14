import random as rand
import time as t
a = []
rand.seed(0)
size = int(input ("Size: "))
for x in range (0, size):
    e = rand.randint(0, 100)
    a.append(e)

print (a)

# [150, 25, 100, 1, 51, 125, -2, 0, 55] (Size = 9)
# [0,   1,  2,   3,  4,   5,  6, 7,  8]

a2 = a

def insertionSort (arr):
    for x in range (1, len(arr)-1):
        j = x
        while j>0 and arr[j-1]>=arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j-=1
            print(arr)

    return arr

'''
working:

initial = [35, 56, 58, 56, 80, 25, 44, 29, 48, 29]
Step 1 =  [25, 56, 58, 56, 80, 35, 44, 29, 48, 29]
'''
print (insertionSort(a))