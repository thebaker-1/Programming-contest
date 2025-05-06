# Problem: Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, size):
        self.parent = { i:i for i in range(1,size+1)}
        self.size = { i:1 for i in range(1,size+1)}
        # print(self.parent)
        # self.parent = [i for i in range(size+1)] # Using dictionary
        # self.size = [1 for i in range(size+1)]

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

def solve():

    n, m, k = map(int, input().split())
    uf = UnionFind(n)
    for _ in range(m):
        u, v = map(int, input().split())
    queries = []
    for _ in range(k):
        q, u, v = map(str, input().split())
        queries.append((q,int(u),int(v)))

    res = []
    queries = queries[::-1]
    for q,u,v in queries:
        if q == "cut":
            uf.union(u,v)
        else:
            if uf.find(u) == uf.find(v):
                res.append("YES")
            else:
                res.append("NO")
    res = res[::-1]
    for i in res:
        print(i)

def main():
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()