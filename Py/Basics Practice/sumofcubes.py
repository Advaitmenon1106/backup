def cube(c):
    return c*c*c

def sumOfCubes(n):
    sum = 0
    for y in range (0, n):
        sum = sum+cube(y+1)
    return sum

num = int (input ("Enter a number: "))

print (sumOfCubes(num))