import random as rand
import time as t

t1 = t.time()

sumArray = []
sumFreq = {}

for x in range (1000000):
    randomSum = rand.randint(2, 12)
    sumArray.append (randomSum)

for x in sumArray:
    if x in sumFreq:
        sumFreq[x]+=1
    else :
        sumFreq[x] = 1

print (sumFreq)
for key, value in sorted(sumFreq.items()):
    print(key, value)
t2 = t.time()
print (t2-t1)