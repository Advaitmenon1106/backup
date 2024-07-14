upperBound = int(input ("Enter an upper bound: "))
lowerBound = int(input ("Enter a lower bound: "))

def primeOrNot(n):
    for x in range (2,n-1):
        if n%x == 0:
            return False
            break
        else:
            continue
    return True

def printPrimes(l,u):
    for x in range (l, u):
        if primeOrNot(x):
            print(x)

printPrimes(lowerBound, upperBound)

# Why is the import feature not working properly?