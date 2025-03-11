# Problem: A - The Ticket Booth - https://codeforces.com/gym/594077/problem/A

import sys
input = sys.stdin.readline

def solve():
    # n = int(input())
    # Read two integers separated by space
    n, m = map(int, input().split())
    if m % n :
        print(m // n + 1)
    else:
        print(m // n)
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