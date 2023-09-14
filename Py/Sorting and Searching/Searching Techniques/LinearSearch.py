array = []
import random as rand
import time as t
size = int(input ("Enter the size of array: "))

"""
for i in range (0, size):
    element = int(input("Enter an element: "))
    array.append (element)

"""
for x in range (0, size):
    e= rand.randint(0, 100)
    array.append(e)

print (array)
search = int(input ("Search for an element: "))
t1 = t.time()

for j in range (0, size):
    if array[j] == search :
        print ("Element is in position ", j+1)

t2 = t.time()
print (t2-t1)