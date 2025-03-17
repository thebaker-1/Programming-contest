# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        def rec(n):
            if n <= 1:
                return n
            return rec(n-1) + rec(n-2)
        return rec(n)