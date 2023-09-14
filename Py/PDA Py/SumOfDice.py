import random as rand
import numpy as np
import pandas as pd

sumArray = []
sumFreq = {}

for x in range (1000000):
    randomSum = rand.randint(0, 12)
    sumArray.append (randomSum)

print (sumArray)