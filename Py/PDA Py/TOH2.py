def ToH(n, Source, Destination, Temp):
    if n == 0:
        return
    elif n == 1: 
        print("Move disk", n, 'from', Source, 'to', Destination)
    else:
        ToH(n-2, Source, Destination, Temp) 
        print("Move disk", n-1, 'from', Source, 'to', Temp)
        ToH(n-2, Destination, Temp, Source)
        print ("Move disk", n, "from", Source, "to", Destination)
        ToH(n-2, Temp, Source, Destination)
        print ("Move disk", n-1, "from", Temp, "to", Destination)
        ToH(n-2, Source, Destination, Temp)

n = int(input('Enter number of disks: '))
ToH(n, "A", "B", "C")

# mathematical induction proof- check