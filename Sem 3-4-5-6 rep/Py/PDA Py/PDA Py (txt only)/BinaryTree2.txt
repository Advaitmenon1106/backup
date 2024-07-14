class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
    
    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left == None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right == None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.data = val

    def preOrder(self):
        print(self.val, end= " ")
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print(self.val, end= " ")
        if self.right:
            self.right.inOrder()

    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.val, end=" ")

root = int(input("Enter a root: "))
newNode = Node(root)
s = int(input("Enter the length: "))
for x in range (0, s):
    e = int(input("Enter an element: "))
    newNode.insert(e)

newNode.inOrder()
print ("\n")
newNode.preOrder()
print ("\n")
newNode.postOrder()
print ("\n")