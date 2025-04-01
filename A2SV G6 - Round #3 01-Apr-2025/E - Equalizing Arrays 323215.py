# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

from itertools import accumulate
import sys
# input = sys.stdin.readline

def solve():
    n = int(input())
    # Read two integers separated by space
    # n, m = map(int, input().split())
    # Read a list of integers separated by space
    nums = list(map(int, input().split()))
    m = int(input())
    nums2 = list(map(int, input().split()))
    a= list(accumulate(nums))
    b = list(accumulate(nums2))
    res = (len(set(a) & set(b)))
    if res and a[-1] == b[-1]:
        print(res)
    else:
        print(-1)


def main():
    # t = int(input())
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()