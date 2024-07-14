from numpy import square


def squareNumber(x):
    return x*x

num = int(input("Enter a number: "))

def sumOfSquares(n):
    sum = 0
    for y in range (0, n+1):
        sum = sum+squareNumber(y)
    return sum

print (sumOfSquares(num))