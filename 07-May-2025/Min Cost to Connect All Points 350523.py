# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class UnionFind:
    def __init__(self, size):
        self.parent = { i:i for i in range(size+1)}
        self.size = { i:1 for i in range(size+1)}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

		
    def union(self, x, y):
        parx = self.find(x)
        pary = self.find(y)
        if parx != pary:
            if self.size[parx] >= self.size[pary]:
                self.parent[pary] = parx
                self.size[parx] += self.size[pary]
            else:
                self.parent[parx] = pary
                self.size[pary]  += self.size[parx]
            return True
                
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        q = []
        uf = UnionFind(len(points))
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                q.append((weight,i,j))       
        q.sort()
        sums = 0
        for weight,i,j in q:
            if uf.union(i,j):
                sums += weight
        return sums