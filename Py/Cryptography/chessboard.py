import numpy as np
import random

n = int(input("Enter a size: "))

board = np.zeroes((n, n), dtype = bytes)

def insertRandom(npArr):
    random.randint(0,n)