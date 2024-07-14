import numpy as np
dataElements = []
left = []
right = []
class node:
    def __init__(self) -> None:
        self.data = None
        self.left = None
        self.right = None
    def createRoot(self, dataEl):
        self.data = dataEl[0]
        self.root = self.data
    def createNode(self, arr):
        s = len(arr)
        flag = 1
        self.left = arr[left[s-1]]
        self.right = arr[right[s-1]]
        while (flag!=s): #traverse all lists, follow algo
            pass
    def displayRootData(self):
        return self.root #change this later; use recursion
    
newNode = node()
newNode.createRoot(dataElements)
#while (c!= len(data)):
#    newNode.data = data[c]
#    newNode.left = None
#    newNode.right = None