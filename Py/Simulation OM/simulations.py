import time
import numpy as np
import pandas as pd
import random as rand
# Columns:-
# Production/Discrete Variables     Probability (Given)      Cumulative Probability        Random Number Interval

def fractionalPart(n):
    whole = n//1
    frac = n-whole
    return frac

Discrete = list(map(float, input().split()))
Probability = list(map(float, input().split()))
size = int(input("How many testing cases: "))
t1 = time.time()
Cumulative = []
flag = 0
for x in range (0, len(Probability)):
    Cumulative.append(flag+Probability[x])
    flag = Probability[x]+flag

Fraction = []
for y in range (0, len(Cumulative)-1):
    el = fractionalPart(Cumulative[y])
    Fraction.append(el*100)
Fraction.append(100)

Range = []
if Fraction[0] == 0:
        Range.append(str(00))
else:
    el1 = str(00)+ "-"
    el2 = str(Fraction[0]-1)
    Range.append(str(el1 + el2))

for z in range (0, len(Cumulative)-1):
    ele1 = str(Fraction[z])+"-"
    ele2 = str(Fraction[z+1]-1)
    Range.append (str(ele1+ele2))

df = pd.DataFrame({
    "Discrete Values" : Discrete,
    "Probability": Probability,
    "Cumulative" : Cumulative,
    "Fractional Part" : Fraction,
    "Random Number Interval" : Range
})

print (df)

randomNumbers = []
for x in range (0, size):
    r = rand.randint(0, 99)
    randomNumbers.append(r)

keyArray = []
keyArray.append(0)
for key in Fraction:
    keyArray.append(key)

simulatedDemand = []
for b in range (0, len(randomNumbers)):
    for c in range (0, len(keyArray)-1):
        if randomNumbers[b]>= keyArray[c] and randomNumbers[b]< keyArray[c+1]:
            simulatedDemand.append(keyArray[c])

#creating a days array for dataframe 2
days = []
for d in range (0, size):
    days.append(d+1)

#Linking Discrete values to bin value (bin contains lower limit of each interval)
simulatedDemandF = {}
for w in range (0, len(Discrete)):
    simulatedDemandF[keyArray[w]] = Discrete[w]

# TO-DO next: use the above linkage and by navigating through the random number column/list...
#... assign a new list for allocation of Discrete values to each random value generated

simulatedDemand2 = []

for r1 in range (0, len(randomNumbers)):
    for r2 in range (0, len(keyArray)-1):
        if keyArray[r2] <= randomNumbers[r1] and keyArray[r2+1]>randomNumbers[r1]:
            simulatedDemand2.append(simulatedDemandF[keyArray[r2]])

df2 = pd.DataFrame({
    "Discrete Values": days,
    "Random Number" : randomNumbers,
    "Interval of Demand" : simulatedDemand,
    "Simulated Demand" : simulatedDemand2
})
print (df2)
t2 = time.time()
print ("Average demand: ", sum(simulatedDemand2)/size)
print ("Time Taken: ", t2-t1)