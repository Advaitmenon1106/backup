import numpy as np
import random

n = int(input("Enter a size: "))

board = np.zeros((n, n), dtype = bytes)

def insertRandom(npArr):
    counter = 0
    for i in range (0, n):
        for j in range (0, n):
            pos = random.randint(0,n*n)
            if pos%n == 0:
                npArr[(pos//n)-1][n-1] = 1
            else:
                npArr[(pos//n)][(pos%n)-1] = 1
    print (npArr)

insertRandom(board)