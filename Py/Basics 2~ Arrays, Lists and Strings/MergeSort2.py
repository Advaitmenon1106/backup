list1 = []
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

newList = list1.append(list2)