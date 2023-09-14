import time

stack = []
timeInitial = time.time()
f = open("C:\\Users\\Kavita manoj\\OneDrive\\Desktop\\PDA Py\\tests\\51")
expression = f.read()
for x in expression:
    stack.append(x)
top = -1

for x in expression:
    if x == '[' or x == '(' or x == '{':
        stack.append(x)
        top+=1
    elif stack[top] == '[' and x == ']':
        stack.pop()
        top-=1
    elif stack [top] == '(' and x == ')':
        stack.pop()
        top-=1
    elif stack[top] == '{' and x == '}':
        stack.pop()
        top-=1

if top == -1:
    print ("Balanced")
else:
    print ("Unbalanced")

timeFinal = time.time()
print ("Time taken = ", timeFinal-timeInitial)
print ("for total string length", len(expression))