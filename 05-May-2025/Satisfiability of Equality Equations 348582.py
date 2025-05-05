# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size+1)] # Using dictionary
        self.size = [1 for i in range(size+1)]

    def find(self, x):
        # Write your code here
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

		
    def union(self, x, y):
        # Write your code here
        parx = self.find(x)
        pary = self.find(y)
        if parx != pary:
            if self.size[parx] >= self.size[pary]:
                self.parent[pary] = parx
                self.size[parx] += self.size[pary]
            else:
                self.parent[parx] = pary
                self.size[pary]  += self.size[parx]
                

    def connected(self, x, y):
        return self.find(x) == self.find(y)
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equal = []
        not_equal = []
        for i in range(len(equations)):
            l1 = ord(equations[i][0])- ord("a")
            l2 = ord(equations[i][3])-ord("a")
            equality = equations[i][1]
            if equality == "=":
                equal.append((l1,l2))
            else:
                not_equal.append((l1,l2))
        uf = UnionFind(27)
        for u,v in equal:
            uf.union(u,v)
        for u,v in not_equal:
            if uf.find(u) == uf.find(v):
                return False
        return True


