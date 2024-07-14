stack = []

def isEmpty():
    if len(stack) == 0:
        return True
    else:
        return False

def push(n):
    stack.append(n)

def pop():
    if isEmpty():
        print("Stack is empty.")
    else:
        stack.pop()

def display():
    if isEmpty():
        print ("Stack is empty")
    else:
        print (stack)

while True:
    choice = int (input("Make a choice: "))
    if choice == 1:
        num = int(input("Enter an element to be input in the stack: "))
        push(num)
    elif choice == 2:
        pop()
    elif choice == 3:
        display()