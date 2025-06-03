# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque
import sys
input = sys.stdin.readline

def solve():
    n, limit = map(int, input().split())
    nums = list(map(int, input().split()))
    smallest = deque()
    largest = deque()
    mini = 0 
    count_segment = 0
    for idx, num in enumerate(nums):
        while smallest and nums[smallest[-1]] >= num:
            smallest.pop()
        smallest.append(idx)
        while largest and nums[largest[-1]] <= num:
            largest.pop()
        largest.append(idx)

        while nums[largest[0]] - nums[smallest[0]] > limit:
            mini += 1
            if largest[0] < mini:
                largest.popleft()
            if smallest[0] < mini:
                smallest.popleft()
        count_segment += idx - mini + 1
    print(count_segment)
    

def main():
    # t = int(input())
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()