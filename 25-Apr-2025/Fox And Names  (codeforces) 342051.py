# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    words = []
    for _ in range(n):
        word = input().strip()
        words.append(word)
    # print(words)
    graph = defaultdict(list)
    indegree = defaultdict(int)
    res = ""
    for k in range(1,n):
        second = words[k]
        first = words[k-1]
        # print(first,second)
        i = 0
        j = 0
        found_res = False
        while i<len(first) and j< len(second):
            # print(first,second,first[i],second[j])
            if first[i] == second[j]:
                i += 1
                j += 1
            else:
                graph[first[i]].append(second[j])
                indegree[second[j]] += 1
                found_res = True
                break

        if not found_res and j == len(second):
            res = "Impossible"
    if res != "Impossible":
        q = deque()
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i not in indegree:
                q.append(i)
        order = []
        while q:
            letter = q.popleft()
            order.append(letter)
            for child in graph[letter]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
        if len(order) == 26:
            print("".join(order))
        else:
            print("Impossible")

    else:
        print("Impossible")

        

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