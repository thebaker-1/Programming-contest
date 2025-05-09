# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class UnionFind:
    def __init__(self, size):
        self.parent = { i:i for i in range(size)}
        self.size = { i:1 for i in range(size)}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
		
    def union(self, x, y):
        parx = self.find(x)
        pary = self.find(y)
        if parx == pary:
            return False
        if self.size[parx] >= self.size[pary]:
            self.parent[pary] = parx
            self.size[parx] += self.size[pary]
        else:
            self.parent[parx] = pary
            self.size[pary]  += self.size[parx]
        return True

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        words = []
        for word in strs:
            strsset = set()
            for i,letter in enumerate(word):
                strsset.add((i,letter))
            words.append(strsset)

        uf = UnionFind(len(strs))
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if uf.find(i) != uf.find(j):
                    differ = words[i] ^ words[j]
                    if len(differ) <= 4:
                        uf.union(i,j)

        group_count = 0
        for i,val in uf.parent.items():
            if i == val:
                group_count += 1
        return group_count