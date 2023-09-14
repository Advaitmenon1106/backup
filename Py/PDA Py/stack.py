class node:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data

class stack:
    def __init__(self) -> None:
        self.top = None
        self.index = 0
    def push(self, el):
        if self.top == None:
            self.index = 0
            self.top = node(el)
        else:
            self.index += 1
            self.top.next = node(el)
            self.top = self.top.next
    def pop(self):
        if self.top == None:
            print ("Underflow")
        else:
            pass
    def display(self):
        print (self.index)
        print (self.top.data)
        pass

s = stack()
s.push(1)
s.push(2)
s.push(3)
s.push(100)
s.display() #shows head data, now figure out a way to display whole stack