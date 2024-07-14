n = int(input ("Enter number of elements in the arrays: "))

arr1 = []
arr2 = []
arr3 = []

print ("Enter elements of first array:- ")

for x in range (0,n):
    element1 = int(input())
    arr1.append(element1)


print ("Enter elements of second array:- ")

for x in range (0,n):
    element2 = int(input())
    arr2.append(element2)

print (arr1); print (arr2)

for x in range (0,n-1):
    element3 = arr1[x]+arr2[x]
    arr3.append(element3)

print(arr3)