import time as t


bitArray = []

def reverse(arr):
    reversedArray = []
    length = len(arr)
    for x in range (0, length):
        el = arr.pop()
        reversedArray.append(el)
    for y in range (length):
        print (reversedArray[y], end = "")
        
def intToBit(n):
    if n==0:
        bitArray.append(n)
    elif n == 1:
        bitArray.append(n)
    else :
        bitArray.append(n%2)
        intToBit(n//2)

start = t.time()
intToBit(100)
reverse(bitArray)
print ("")
print(t.time()- start)

start2 = t.time()
print ("")
print(bin(100))
print ("")
print (t.time() - start2)