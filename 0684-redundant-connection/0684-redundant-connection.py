class UnionFind:
    def __init__(self,size):
        self.root = list(range(size))
        self.rank = [0]* size
    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        res = []
        uf = UnionFind(len(edges)+1)
        print(uf.root)
        for u,v in edges:
            print(1)
            if uf.find(u) != uf.find(v):
                print(2)
                uf.union(u,v)
            else:
                res = [u,v]
        return res
        