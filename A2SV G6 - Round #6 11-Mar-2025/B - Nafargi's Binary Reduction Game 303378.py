# Problem: B - Nafargi's Binary Reduction Game - https://codeforces.com/gym/594077/problem/B

import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    m = input()
    m = list(str(i) for i in m)
    one = m.count("0")
    zero = m.count("1")
    print(abs(one-zero))


    # Read two integers separated by space
    # n, m = map(int, input().split())
    # Read a list of integers separated by space
    # nums = list(map(int, input().split()))
    # Read a list of integers separated by a comma
    # nums = list(map(int, input().split(',')))
    # Read a list of words separated by space
    # words = input().split()
    # Read a list of words separated by a comma
    # words = input().split(',')
    

def main():
    # t = int(input())
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()