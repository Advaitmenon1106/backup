array = []

def monotonicOrNot(arr, s):
    Array1 = []
    Array2 = []
    Array3 = []
    for x in range(0,s-1):
        count = arr[x]
        if count > arr[x+1]:
            Array1.append(1)
        elif count < arr[x+1]:
            Array2.append(1)
        elif count == arr[x+1]:
            Array3.append(2)
    if len(Array1) == 0:
        print ("Monotonic")
    elif len(Array2) == 0:
        print ("Monotonic")
    else:
        print ("Not monotonic")

size = int(input("Enter the size of your array: "))

for i in range (0, size):
    element = int (input ("Insert an element: "))
    array.append(element)

monotonicOrNot(array, size)