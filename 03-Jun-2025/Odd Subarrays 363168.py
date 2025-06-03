# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    odd_count = 0
    pass_now = False
    for i in range(1,len(nums)):
        if pass_now:
            pass_now = False
            continue
        if nums[i] < nums[i-1]:
            odd_count += 1
            pass_now = True
            
    print(odd_count)
    

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()