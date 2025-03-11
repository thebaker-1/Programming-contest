# Problem: B - Kidus Couldn't Sleep - https://codeforces.com/gym/589822/problem/B

import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    l = 0
    sum_sep = sum(nums[:m])
    sum_t = sum_sep
    for r in range(m,len(nums)):
        sum_sep += nums[r] - nums[l]
        sum_t += sum_sep
        l += 1
    print(sum_t / (n-m+1))


def main():
    # t = int(input())
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()