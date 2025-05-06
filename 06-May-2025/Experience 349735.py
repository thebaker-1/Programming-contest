# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

import sys
input = sys.stdin.readline
import sys
input = sys.stdin.readline
from collections import defaultdict
import sys
input = sys.stdin.readline
# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.parent = { i:i for i in range(size+1)}
        self.size = { i:1 for i in range(size+1)}
        self.weight = defaultdict(int)


    def find(self, x):
        # Write your code here
        if self.parent[x] != x:
            return self.find(self.parent[x])
        return self.parent[x]
	
    def union(self, x, y):
        parx = self.find(x)
        pary = self.find(y)
        if parx != pary:
            if self.size[parx] >= self.size[pary]:
                self.parent[pary] = parx
                self.weight[pary] -= self.weight[parx]
                self.size[parx] += self.size[pary]
            else:
                self.parent[parx] = pary
                self.weight[parx] -= self.weight[pary]
                self.size[pary] += self.size[parx]
            

    def get(self, x):
        res = self.weight[x]
        while self.parent[x] != x:
            res += self.weight[self.parent[x]]
            x = self.parent[x] 
        # print(self.weight)
        return res           



def solve():
    # n = int(input())
    # Read two integers separated by space
    n, m = map(int, input().split())
    uf = UnionFind(n)
    for _ in range(m):
        q = input().split()


        if q[0] == "add":
            u = uf.find(int(q[1]))
            uf.weight[u] += int(q[2])
            # print(u,uf.weight[u])
        elif q[0] == "join":
            uf.union(int(q[1]),int(q[2]))
        else:
            print(uf.get(int(q[1])))

    # Read a list of integers separated by space
    # nums = list(map(int, input().split()))
    # Read a list of integers separated by a comma
    # nums = list(map(int, input().split(',')))
    # Read a list of words separated by space
    # words = input().split()
    # Read a list of words separated by a comma
    # words = input().split(',')
    

def main():
    # t = int(input())
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()