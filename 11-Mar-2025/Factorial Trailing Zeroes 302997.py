# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fib(n):
            if n == 1 or n == 0: return 1
            return n * fib(n-1)
        word = (fib(n))
        
        count = 0
        while word:
            if word % 10:
                break
            word //= 10
            count += 1
        return count
        