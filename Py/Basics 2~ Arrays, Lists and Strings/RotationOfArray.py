array = []
size = int (input ("Enter the size of the array"))
for i in range (0, size):
    element = int (input ("Insert an element: "))
    array.append(element)

print (array)

def Rotate(arr, d):
    temp = []
    for j in range (d, size):
        element2 = array[j]
        temp.append(element2)
    for k in range (0, d):
        element3 = array[k]
        temp.append(element3)
    return temp

swap = int(input ("Enter the position from which you want to swap the array: "))
rotated = Rotate(array, swap)
print (rotated)