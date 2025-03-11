# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def rec(n):
            if n == 1:
                return [0]
                
            res = rec(n-1)
            return res + [1] + [0 if i else 1 for i in res][::-1]
        arr = rec(n)
        return str(arr[k-1])
        