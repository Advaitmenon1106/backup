# Question: Array of numbers, terminating character is *, find the second largest number

array = []
element = 50

while(True): 
    element = input("Enter an element: ")
    if element == '*':
        break
    else:
        array.append(int(element))

def findLargest(arr):
    count = arr[0]
    size = len(arr)
    for x in range (0, size):
        if arr[x-1] > count:
            count = arr[x-1]
    return count

lar1 = findLargest(array)
array.remove(lar1)
lar2 = findLargest(array)
print (lar2)