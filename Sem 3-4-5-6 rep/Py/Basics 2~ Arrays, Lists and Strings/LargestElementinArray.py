arr1 = []
size = int(input("Enter the size of your array: "))
print ("Input elements of the array:-")

for x in range (0,size):
    element = int (input())
    arr1.append(element)


flag = arr1[0]

for y in range (0,size):
    if arr1[y] > flag:
        flag = arr1[y]


print (flag, "is the largest element in the array.")    