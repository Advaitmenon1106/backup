import numpy as np
import random

n = int(input("Enter a size: "))

board = np.zeros((n, n), dtype = int)

def insertRandom(npArr):
    counter = 0
    for i in range (0, n):
        for j in range (0, n):
            pos = random.randint(0,n*n)
            if pos%n == 0:
                npArr[(pos//n)-1][n-1] = 1
                print(pos)
            else:
                npArr[(pos//n)][(pos%n)-1] = 1
                print (pos)
    print (npArr)

# allocation done

sequence = ""

def edges(arr):
    global sequence
    for t in range (1, n-1):
        if arr[0, t] == 1:
            sequence+= str(t)
        elif arr[n-1][t] == 1:
            sequence+= str((7*(n-1))+t)


# checking if it is an edge or a corner point

def adjacentOrNot(ar):
    global sequence
    for u in range (1, n-1):
        for v in range (1, n-1):
            if edges(ar):
                if ar[u][v+1] == 1: 
                    sequence += str()
                elif ar[u][v-1] == 1:
                    sequence+= str()
            elif ar[u][v+1] == 1:
                return True
            elif ar[u][v-1] == 1:
                return True
            elif ar[u-1][v] == 1:
                return True
            elif ar[u+1][v] == 1:
                return True
insertRandom(board)
edges(board)
adjacentOrNot(board)

print (sequence)