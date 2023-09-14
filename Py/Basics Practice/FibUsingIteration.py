import time
timeInitial = time.time()
digits = []
def fib(n):
    initial = 0
    next = 1
    if n == 0:
        return initial
    elif n == 1:
        return next
    else:
        for x in range (2, 61):
            fibNo = initial+next
            digits.append(fibNo%10)
            initial = next
            next = fibNo
    return digits[n%60] #n = 78395, length = 16384

num = int(input("Enter a number: "))
fibFinal = fib(num)
print (fibFinal)
print (digits)
print ("Length = ", len(str(fibFinal)))
timeFinal = time.time()
print (timeFinal-timeInitial)