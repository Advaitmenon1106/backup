array = []
size = int (input ("Enter the number of elements in the array: "))

for i in range (0, size-1):
    element = int(input ("Enter an element: "))
    array.append(element)

print (array)

sum = 0
for j in range (0, size-1):
    sum = sum+array[j]

print (str (sum) + " is the sum of all elements in the array.")