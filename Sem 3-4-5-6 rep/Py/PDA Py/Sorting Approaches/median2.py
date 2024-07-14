import random as rand

n = input()
array1 = []
for x in range (0, n):
    elements = rand.randint(0, 100)
    array1.append(elements)

print (array1)

def insertion(a):
    for x in range (1, len(a)):
        flag = a[x]
        j = x-1
        while j>=0 and flag <a[j]:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = flag

insertion(array1)
print (array1)

''
if len(array1)%2 == 0:
    median = (array1[len(array1)/2]+array1[(len(array1)+2)/2])/2
else:
    median = array1[(len(array1)+1)/2]

print (median)

''