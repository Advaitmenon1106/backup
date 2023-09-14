l = int (input())
r = int(input())
k = int (input())

counter = 0

for x in range (1,l):
    for y in range (1,r):
        for z in range (1,k):
            a = l%x
            b = r%y
            c = k%z
            if a == b and b == c and c == a:
                counter = counter + 1
                print (counter)

print (counter)