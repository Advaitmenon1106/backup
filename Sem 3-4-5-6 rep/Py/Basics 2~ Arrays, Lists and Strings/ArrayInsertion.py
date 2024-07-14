def rightShift(arr, ins, posIndex):
    l = len(arr)
    temp = []
    for x in range (0, l):
        if x == posIndex:
            temp.append(ins)
            for y in range (x, l):
                temp.append(arr[y])
            break
        else:
            temp.append(arr[x])            
    arr = temp
    del temp
    return arr

array1 = [1, 2, 3, 4, 5, 6]
print (array1)
insert = int(input("Enter a number to be inserted: "))
position = int(input ("Enter th position: "))
array2 = rightShift(array1, insert, position-1)
print (array2)