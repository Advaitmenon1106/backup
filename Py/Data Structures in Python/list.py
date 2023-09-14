list = []
while(True):
    choice = int(input("Make a choice: "))
    if choice == 1 :
        element = input()
        list.append(element)
    elif choice == 2:
        list.pop()
    elif choice == 3:
        print (list)
