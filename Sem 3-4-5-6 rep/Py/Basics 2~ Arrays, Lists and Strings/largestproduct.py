import time

time1 = time.time()
def largest(arr):
    l1 = len(arr)
    flag = arr[0]
    for i in range (0, l1):
        if arr[i]>flag:
            flag = arr[i]
    return flag

def secondLargest(arr2):
    arr3 = arr2
    largest1 = largest(arr3)
    arr3.remove(largest1)
    secondLargestElement = largest(arr3)
    return secondLargestElement

array = []
size = int(input("Enter the size of your array: "))
print ("Input elements of the array:-")

for x in range (0,size):
    element = int (input())
    array.append(element)

max = largest(array)
secondMax = secondLargest(array)
print (max*secondMax)
print (array)
time2 = time.time()
print (time2 - time1)