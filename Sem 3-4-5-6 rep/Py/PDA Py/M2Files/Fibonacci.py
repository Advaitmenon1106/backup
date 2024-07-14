import time
timeInitial = time.time()
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
            initial = next
            next = fibNo
    return next #n = 78395, length = 16384

num = int(input("Enter a number: "))
fibFinal = fib(num)
print (fibFinal)
print (fibFinal%10)
fibFinalStr = str(fibFinal)
print (fibFinalStr[len(fibFinalStr)-1])
print ("Length = ", len(str(fibFinal)))
timeFinal = time.time()
print (timeFinal-timeInitial)