array = []
size = int (input ("Enter the size of the array"))
for i in range (0, size):
    element = int (input ("Insert an element: "))
    array.append(element)

print (array)

divisor = int(input("Enter a divisor: "))

product = 1

for i in range (0, size):
    product = product*array[i]

print ("The quotient is " + str(product/divisor) + ", and the remainder is " + str(product%divisor))