import time
timeInitial = time.time()
def fibonacci(n):
    if (n == 0 or n == 1):
        return n
    else :
        return (fibonacci(n-1) + fibonacci(n-2))

num = int (input ("Enter a number: "))
nthFibNo = fibonacci(num)
timeFinal = time.time()
print ("Time taken: ", timeFinal-timeInitial)