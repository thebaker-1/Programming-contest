# Problem: A - Kibr and His Musics - https://codeforces.com/gym/589822/problem/A

from bisect import bisect_left
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    sums = 0
    res = []
    for _ in range(n):
        c,t  = map(int, input().split())
        sums += c*t
        res.append(sums)

    queries = list(map(int,input().split()))
    for querie in queries:
        print(bisect_left(res,querie) + 1)

    

def main():
    # t = int(input())
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()