# Problem: A - A+ Student - https://codeforces.com/gym/590053/problem/A

import sys
input = sys.stdin.readline

def solve():
    a,b,c= map(int, input().split())
    res = []
    if max(b,c) >= a:
        res.append(max(b,c) - a + 1)
    else:
        res.append(0)
    if max(a,c) >= b:
        res.append(max(a,c) - b + 1)
    else:
        res.append(0)
    if max(a,b) >= c:
        res.append(max(a,b) - c+1)
    else:
        res.append(0)
    print(*res)


def main():
    t = int(input())
    #t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()