import random
array = []
size = int(input("Enter a size: "))
c = 0
while (c!=size):
    rand = random.randint(0, 100)
    array.append(rand)
    c+=1

pivot = array[0]

def partition(a, lo, hi):
    i = lo + 1
    j = hi
    while True:
        while a[i]<a[lo]:
            if i == hi:
                break
            i+=1
        while a[lo]<= a[j]:
            if j==lo: break
            j-=1
