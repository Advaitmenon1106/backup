class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None

    def enqueue(self, data):
        if self.front == None:
            self.front = node(data)
            self.rear = self.front
        else:
            self.rear.next = node(data)
            self.rear = self.rear.next 
    def dequeue(self):
        if self.front == None:
            print ("Underflow")
        else:
            toDelete = self.front
            self.front = self.front.next
            del toDelete
    
    def display(self):
        if self.front == None:
            print ("Empty")
        else:
            traverse = self.front
            while (traverse!= self.rear):
                print (traverse.data)
                traverse = traverse.next
            print (traverse.data)
    
queue1 = queue()
choice = 0
while (choice != 4):
    choice = int(input("Make a choice {1: Enqueue | 2: Dequeue | 3: Display | 4: Quit}: "))
    if choice == 1:
        element = int(input("Insert element to be enqueued: "))
        queue1.enqueue(element)
    elif choice == 2:
        queue1.dequeue()
    elif choice == 3:
        print ("Head: ", queue1.front.data)
        print ("Tail: ", queue1.rear.data)
        queue1.display()