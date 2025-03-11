# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res=  [0]*(len(temperatures))
        for i,val in enumerate(temperatures[::-1]):
            if not stack:
                stack.append((i,val))
                res[-i-1] = 0
                continue
            while stack and stack[-1][1] <= val:
                stack.pop()
            stack.append((i,val))
            if len(stack) == 1:
                res[-i-1] = 0
            else:
                res[-i-1] = stack[-1][0] - stack[-2][0]
        return res
