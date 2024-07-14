# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi]. 
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes 
# the absolute value of val. Return the minimum cost to make all points connected. 
# All points are connected if there is exactly one simple path between any two points.

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def minCostConnectPoints(points):
    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    n = len(points)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            distance = manhattan_distance(points[i], points[j])
            edges.append((i, j, distance))

    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    min_cost = 0
    for edge in edges:
        u, v, cost = edge
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            min_cost += cost

    return min_cost

# Example usage:
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(minCostConnectPoints(points))
