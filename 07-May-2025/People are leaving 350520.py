# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, size):
        self.parent = { i:i for i in range(size+1)}
        self.size = { i:1 for i in range(size+1)}


    def find(self, x):

        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]

		
    def union(self, x, y):
        parx = self.find(x)
        pary = self.find(y)
        if parx != pary:
            if parx > pary:
                parx, pary = pary, parx
            self.parent[parx] = pary
  
    def connected(self, x, y):
        return self.find(x) == self.find(y)

def solve():

    n, m = map(int, input().split())
    q = []
    uf = UnionFind(n)
    visited = set()
    for _ in range(m):
        askorleave, u = map(str, input().split())
        u = int(u)
        if askorleave == "?":
            if u not in visited:
                print(u)
            else:
                res = uf.find(u) + 1
                if res <= n:
                    print(res)
                else:
                    print(-1)
        else:
            if u + 1 in visited:
                uf.union(u,u+1)
            if u - 1 in visited:
                uf.union(u,u-1)
            visited.add(u)

def main():
    # t = int(input())
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()