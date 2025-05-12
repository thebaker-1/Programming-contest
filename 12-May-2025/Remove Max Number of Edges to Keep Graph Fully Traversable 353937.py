# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class UnionFind:
    def __init__(self, size):
        self.parent = { i:i for i in range(1,size)}
        self.size = { i:1 for i in range(1,size)}

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
                
    def connected(self, x, y):
        return self.find(x) == self.find(y)
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(reverse = True)
        alice = UnionFind(n + 1)
        bob = UnionFind(n + 1)
        count = 0
        for i,u,v in edges:
            if i == 3:
                if alice.connected(u,v):
                    count += 1
                else:
                    alice.union(u,v)
                    bob.union(u,v)
            elif i == 2:
                if bob.connected(u,v):
                    count += 1
                else:
                    bob.union(u,v)
            else:
                if alice.connected(u,v):
                    count += 1
                else:
                    alice.union(u,v)

        alice_components = 0
        bob_components = 0
        for i,val in alice.parent.items():
            if i == val:
                alice_components += 1
            if alice_components > 1:
                return -1
        for i,val in bob.parent.items():
            if i == val:
                bob_components += 1
            if  bob_components > 1:
                return -1
        return count

        