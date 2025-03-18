# Problem: D - Creating an a-Good String - https://codeforces.com/gym/596141/problem/D

import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    words = list(input().strip())
    words = [ord(i) - ord("a") for i in words]
    def rec(word,chr):
        if len(word) <= 1:
            if word[0] == chr:
                return 0
            else:
                return 1
        half = len(word)//2
        cost1 = (len(word[:half]) - word[:half].count(chr)) + rec(word[half:],chr + 1)
        cost2 = (len(word[half:]) - word[half:].count(chr)) + rec(word[:half],chr + 1)
        return min(cost1,cost2)

    print(rec(words,0))
    

def main():
    t = int(input())
    #t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()