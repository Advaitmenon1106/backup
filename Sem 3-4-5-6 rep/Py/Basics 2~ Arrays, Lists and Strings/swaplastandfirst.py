array = []

def swapElements(arr):
    s = len(arr)
    temp = arr[s-1]
    arr[s-1] = arr[0]
    arr[0] = temp
    print (array)

size = int(input("Enter the size of your array: "))

for i in range (0, size):
    element = int (input ("Insert an element: "))
    array.append(element)

swapElements(array)