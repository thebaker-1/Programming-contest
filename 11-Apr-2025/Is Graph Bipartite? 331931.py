# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

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
    def isBipartite(self, graph: List[List[int]]) -> bool:
        uf = UnionFind(len(graph))
        for u,nodes in enumerate(graph):
            for v in nodes:
                uf.union(nodes[0],v)
                if uf.find(nodes[0]) == uf.find(u):
                    return False
        return True