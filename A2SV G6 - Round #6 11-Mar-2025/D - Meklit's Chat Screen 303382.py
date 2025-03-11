# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

from collections import deque
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    q = deque()
    unique = set()
    for i in nums:
        if i not in unique:
            if len(q) == m:
                x = q.pop()
                unique.discard(x)
            q.appendleft(i)
            unique.add(i)
    print(len(q))
    print(*q)

    

def main():
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()