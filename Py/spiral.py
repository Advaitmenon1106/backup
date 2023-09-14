import turtle
t = turtle.Pen()

i = int (input("enter a value: "))

for x in range (300):
    t.forward(x)
    t.right(i)
    