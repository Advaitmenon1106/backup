from msilib import datasizemask
import numpy as np
data = [0]
left = [5]
right = [7]
class node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right  = None
    def createRoot(self, dataArr):
        self.data = dataArr[0]
class tree:
    pass
newNode = node()
node.createRoot()
node.displayNodeData()
#while (c!= len(data)):
#    newNode.data = data[c]
#    newNode.left = None
#    newNode.right = None