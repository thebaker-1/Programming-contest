# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class UnionFind:
    def __init__(self,size):
        self.root = list(range(size))
        self.rank = [0]* size
    def find(self, main):
        n= main
        while main != self.root[main]:
            main = self.root[main]
        while n != main:
            nxt = self.root[n]
            self.root[n] = main
            n = nxt
        return main
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
        for u,v in edges:
            if uf.find(u) != uf.find(v):
                uf.union(u,v)
            else:
                res = [u,v]
        return res
        