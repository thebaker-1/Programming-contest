# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    start = 0
    gap = []

    if k == 1:
        print(nums[-1] - nums[0])

    else:
        for i in range(1,len(nums)):
            gap.append((nums[i] - nums[i-1],i))

        gap.sort()
        gap = gap[-k+1:]
        gap.sort(key = lambda x:x[1])

        start = 0
        res1 = 0
        for val, i in gap:
            res1 += nums[i-1] - nums[start]
            start = i
        res1 += nums[-1] - nums[start]

        print(res1)


    

def main():
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
