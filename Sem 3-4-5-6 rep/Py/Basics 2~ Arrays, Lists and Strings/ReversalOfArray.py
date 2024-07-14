array = []
size = int (input ("Enter the size of the array"))
for i in range (0, size):
    element = int (input ("Insert an element: "))
    array.append(element)

print (array)

reverse = []

for i in range (0, size):
    element = array.pop()
    reverse.append(element)

print (reverse)