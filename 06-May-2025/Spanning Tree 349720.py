# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

import sys
input = sys.stdin.readline

# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.parent = { i:i for i in range(size+1)}
        self.size = { i:1 for i in range(size+1)}
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
    # n = int(input())
    # Read two integers separated by space
    n, m = map(int, input().split())
    uf = UnionFind(n)
    lis = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        lis.append((w,u,v))
    lis.sort()
    sum = 0
    for w,u,v in lis:
        if uf.find(u) != uf.find(v):
            uf.union(u,v)
            sum += w
    print(sum)
        

def main():
    # t = int(input())
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()