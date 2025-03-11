# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

from itertools import accumulate
import sys
input = sys.stdin.readline

def solve():
    # n = int(input())
    # Read two integers separated by space
    n, m = map(int, input().split())
    # Read a list of integers separated by space
    nums = list(map(int, input().split()))
    prefix = [0]
    suffix = []
    for i in range(len(nums)-1):
        if nums[i] - nums[i+1] > 0:
            prefix.append(nums[i] - nums[i+1])
        else:
            prefix.append(0)
    for j in range(len(nums)-1,0,-1):
        if nums[j] -nums[j-1] > 0:
            suffix.append(nums[j] -nums[j-1])
        else:
            suffix.append(0)
    suffix.append(0)
    suffix.append(0)
    suffix = suffix[::-1]
    suffix = (list(accumulate(suffix)))
    prefix = list(accumulate(prefix))
    for _ in range(m):
        l,r = map(int, input().split())
        if r > l: 
            print(prefix[r-1]- prefix[l-1])
        else:
            print(suffix[l]- suffix[r])

    

def main():
    # t = int(input())
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()