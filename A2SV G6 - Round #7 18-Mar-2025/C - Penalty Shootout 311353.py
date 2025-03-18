# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

import sys
input = sys.stdin.readline

def solve():
    nums = list(input().strip())
    t1 = 0
    t2 = 0
    qOne = 0
    qTwo = 0
    t1left = 5
    t2left = 5

    for i in range(len(nums)):
        if i% 2:
            t1left -= 1
            if nums[i] == "1":
                t1 += 1
            elif nums[i] == "0":
                pass
            else:
                qOne += 1
        else:
            t2left -= 1
            if nums[i] == "1":
                t2 += 1
            elif nums[i] == "0":
                pass
            else:
                qTwo += 1
        if t1 + qOne > t2left + t2:
            print(i+1)
            break
        elif t2 + qTwo > t1left + t1:
            print(i+1)
            break
    else:
        print(10)

    
    
    

def main():
    t = int(input())
    #t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()