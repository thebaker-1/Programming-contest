# Problem: C - Permutation Minimization - https://codeforces.com/gym/594077/problem/C

from collections import deque
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    q = deque()
    for i in range(len(nums)):
        if not q or nums[i] <= q[0]:
            q.appendleft(nums[i])
        else:
            q.append(nums[i])
    print(*q)
    

def main():
    t = int(input())
    #t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()