def findLargest(arr):
    count = arr[0]
    size = len(arr)
    for x in range (0, size):
        if arr[x-1] > count:
            count = arr[x-1]
    return count

A = []
n = int(input())
for k in range (0,n):
    el = int(input())
    A.append(el)
    
lar1 = findLargest(A)
A.remove (lar1)
lar2 = findLargest(A)
print (lar2)