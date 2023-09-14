a = int (input ("Enter a number: "))

def primeOrNot(n):
    for x in range (2,n-1):
        if n%x == 0:
            return False
            break
        else:
            continue
    return True


if primeOrNot(a):
    print("Number is prime")
else :
    print("Number is composite")