# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

from collections import defaultdict
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    graph = defaultdict(list)
    for i in range(n-1):
        parent = int(input())
        graph[parent].append(i+2)

    for i,vals in graph.items():
        count = 0
        for val in vals:
            if val not in graph:
                count += 1
        if not( count >= 3):
            print("No")
            break
    else:
        print("Yes")

    

def main():
    # t = int(input())
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()