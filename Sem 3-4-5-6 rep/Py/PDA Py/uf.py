import numpy as np

class UF:
    size = 0
    id1 = []
    
    # CONSTUCTOR
    def __init__(self, n):
        self.size = n
        self.id1 = np.arange(n, dtype=int)
    # end of constructor
    
    def find(self, p, q):       # order of 1 or O(1) quick find
        return self.id1[p] == self.id1[q]
    def union(self, p, q):      # order (n) costly
        if self.find(p, q):
            return
        x = self.id1[p]
        for i in range(self.size):
            if self.id1[i] == x:
                self.id1[i] = self.id1[q]
