noOfMovement = 0


def ToH(n, Source, Destination, Temp):
    global noOfMovement
    if n == 1:      # only one disk
        print('Move disk#', n, 'from', Source, 'to', Destination)
        noOfMovement += 1
    else:
        ToH(n-1, Source, Temp, Destination)         # some expert moves n-1 disks from source to temo using destination
        print('Move disk#', n, 'from', Source, 'to', Destination) # physical 1 disk movement
        noOfMovement += 1
        ToH(n-1, Temp, Destination, Source)         # move back n-1 disks which are at temp to destination using course

n = int(input('Enter number of disks: '))
ToH(n, "A", "B", "C")
print('\n No Of Movement: ', noOfMovement)

#mathematical induction- check!!!