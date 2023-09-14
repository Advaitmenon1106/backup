class node():
    def __init__(self, data) -> None:
        self.next = None
        self.data = data

class LinkedList():
    def __init__(self) -> None:
        self.head = None

    def insertNode(self, ins):
        newnode = node(ins)
        if self.head == None:
            self.head = newnode
        else:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr = ptr.next
            ptr = newnode
            print (ptr, "is inserted")
            
    def display(self):
        d = self.head
        while d:
            print (d.data)
            d = d.next

l = LinkedList()
l.insertNode(100)
l.insertNode(6)
l.insertNode(7)
l.insertNode(7)
l.insertNode(7)
l.display()
l.display()