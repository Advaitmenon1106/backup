from re import S
from btds_bitarray import btds_bitarray
from uf import UF
import random as rndm

class board():
    size = None
    no_of_sq_open = 0
    openclose = None
    store = None

    def __board__(self, n):
        self.size = n
        store = UF(n*n+2)
        openclose = btds_bitarray(n*n+2)
        openclose[0] = 1
        openclose[n*n+1] = 1

    def connected(self):
        #return self.board.find(0, n*n+1)
        for i in range (1, self.size+1):
            for j in range(self.size*(self.size-1)+1, self.size+1):
                if self.board.find(i, j):
                    return True
    
    def open_one_sq(self, p):
        if self.opencclose[p]:
                return
        elif self.openclose[p]== 1:
            no_of_sq_open += 1
            self.openclose(p, p+1)
            self.oenclose(p, p-1)
            self.connect(p, p-self.size)

    def print_size(self):
        print(self.size)

    def connect(self, p, q):
        global openclose
        if openclose[p] and openclose[q] == 1:
            self.store.union(p, q)

n = int(input("Enter size: "))

b = board()
while not b.connected():
    x = rndm.randint(1, n*n)
    b.open_one_sq(x)

print(b.no_of_sq_open/(n*n), '%')