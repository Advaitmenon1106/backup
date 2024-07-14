import random as rand

n = 20
array1 = []
for x in range (0, n):
    elements = rand.randint(0, 100)
    array1.append(elements)

print (array1)

sorted = array1
flag = array1[0]
sorted[len(array1)-1] = flag
for x in range (1, len(array1)):
    if array1[x] >= flag:
        sorted[len(array1)-1] = sorted[len(array1)-2]
        flag = array1[x]

print (sorted)