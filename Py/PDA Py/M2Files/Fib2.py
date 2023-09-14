import time as t

tInitial = t.time()

def fib(lt):
    initial = 0
    next = 1
    counter = 1
    if lt == 1:
        return initial
    else:   
        while counter < lt:
            fibNo = initial + next
            initial = next
            next = fibNo
            counter += 1
        return next

num = int(input("Enter: "))
finalVal = fib(num)
print (finalVal%10)
tFinal = t.time()
print (tFinal-tInitial)