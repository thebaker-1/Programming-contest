# Problem: Power of Three - https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def rec(n):
            if n == 1:
                return True
            elif n == 0:
                return False
            elif n / 3 != n // 3:
                return False
            else:
                return rec(n/3)
        return rec(n)
        