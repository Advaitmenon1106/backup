import numpy as np
import random

from chessboard3 import edges

n = int(input("Enter a size: "))

board = np.zeros((n, n), dtype = int)

def insertRandom(npArr):
    counter = 0
    for i in range (0, n):
        for j in range (0, n):
            pos = random.randint(1,n*n)
            if pos%n == 0:
                npArr[(pos//n)-1][n-1] = 1
                print(pos)
            else:
                npArr[(pos//n)][(pos%n)-1] = 1
                print (pos)
    print (npArr)


def corners(arr):
    if arr[0][0] == 1:
        return True
    elif arr[0][n-1] == 1:
        return True
    elif arr[n-1][0] == 1:
        return True 
    elif arr[n-1][n-1] == 0:
        return True
    else:
        return False

def edgesUpperHorizontal(ar):
    for u in range (1, n-1): #travering single row
        if ar[0][u] == 1:
            return True # Top edge, left to right, excluding corners
        else:
            return False

def edgesLowerHorizontal(arr6):
    for p in range (1, n-1):
        if arr6[n-1][p] == 1:
            return True # Bottom edge, l to r, exc. corners
        else :
            return False

def edgesRightVertical(arr4):
    for v in range (1, n-1): #for traversing single column
        if arr4[v][0] == 1: #traversing first column up to down, exc. corner
            return True
        else:
            return False

def edgesLeftVertical(arr7):
    for q in range (1, n-1):
        if arr7[q][n-1] == 1: #traversing last column, up to down, exc. corners
            return True
        else:
            return False

def adjacencyOfCorners(arr2):
    if corners(arr2):
        if arr2[0][1] == 1:
            return True
        elif arr2[1][0] == 1: # for 1st corner point
            return True
        elif arr2[0][n-2] == 1:
            return True
        elif arr2[1][n-1] == 1: # for 2nd corner point
            return True
        elif arr2[n-2][0] == 1:
            return True
        elif arr2[n-1][1] == 1: # for 3rd corner point
            return True
        elif arr2[n-1][n-2] == 1:
            return True
        elif arr2[n-2][n-1] == 1: # for 4th corner point
            return True        
        else:
            return False

def adjacencyOfTopEdges(arr5):
    for r1 in range (1,n-1):
        if edgesUpperHorizontal(arr5):
            pass


for v1 in range (0,n):
    for v2 in range (0,n):
        if adjacencyOfCorners(board):
            pass



insertRandom(board)
checking = adjacencyOfCorners(board)
print (checking)