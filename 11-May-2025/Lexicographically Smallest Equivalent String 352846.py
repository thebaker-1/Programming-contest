# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class UnionFind:
    def __init__(self, size):
        self.parent = { i:i for i in range(size)}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
		
    def union(self, x, y):
        parx = self.find(x)
        pary = self.find(y)
        if parx == pary:
            return False
        elif parx < pary:
            self.parent[pary] = parx
        else:
            self.parent[parx] = pary

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        length = len(s1)
        uf = UnionFind(27)
        for i in range(length):
            uf.union((ord(s1[i]) - ord("a")),(ord(s2[i]) - ord("a")))
        
        newStr = []
        for i in range(len(baseStr)):
            newStr.append(chr(uf.find(ord(baseStr[i]) - ord("a")) + ord("a")))
        return "".join(newStr)

        

        