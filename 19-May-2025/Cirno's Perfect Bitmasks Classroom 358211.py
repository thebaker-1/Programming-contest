# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

import sys
input = sys.stdin.readline

def solve():
    num = int(input().strip())
    new_num = 0
    k = 0
    while not(num & (1<<k)):
        k += 1
    new_num = 1 << k
    if new_num == num:
        k = 0
        while num & (1<<k):
            k += 1
        new_num |= 1<<k
    print(new_num)



def main():
    t = int(input())
    #t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()