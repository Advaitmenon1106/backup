array = []

def swapElements(arr, pos1, pos2):
    temp = arr[pos2-1]
    arr[pos2-1] = arr[pos1-1]
    arr[pos1-1] = temp

size = int(input("Enter the size of your array: "))

for i in range (0, size):
    element = int (input ("Insert an element: "))
    array.append(element)