inputValues = []
prime = []
composite = []
arrayForOne = []

for i in range (0, 5):
    el = int(input("Enter a number: "))
    inputValues.append(el)

print (inputValues)

def primeOrNot(n):
    for x in range (2,n-1):
        if abs(n)%x == 0:
            return False
            break
        else:
            continue
    return True

for j in range (0, 5):
    el2 = inputValues[j]
    if el2 == 1 or el2 == 0 or el2 == -1:
        arrayForOne.append(el2)
        continue       
    if primeOrNot(el2):
        prime.append(el2)
    else:
        composite.append(el2)

print ("prime numbers: ", prime)
print ("composite numbers: ", composite)
print ("one is neither prime nor composite: ", arrayForOne)