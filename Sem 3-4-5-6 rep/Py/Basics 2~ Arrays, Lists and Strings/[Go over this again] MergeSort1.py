def rightShift(arr, ins, posIndex): #arr = target array, ins = element to be inserted/merged, posIndex = target index
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
    print ("Function called, array= ", arr)
    return arr

def merge(a1, a2, i1, i2):
    if a1[i1]>a2[i2]:
        return rightShift(a1, a2[i2], i1)


list1 = [] #target list
list2 = []
size1 = int(input("Enter the size of your first array: "))
print ("Input elements of the first array:-")

for x in range (0,size1):
    element = int (input())
    list1.append(element)

size2 = int(input("Enter the size of your second array: "))
print ("Input elements of the second array:-")

for y in range (0,size2):
    e = int (input())
    list2.append(e)

for z2 in range (0, size2):
    for z1 in range (0, size1):
        if list1[z1]<list2[z2]:
            list1.append(list2[z2])
        else:
            merge(list1, list2, z1, z2)


print (list1)
print (list2)
# print (newArr)