# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0

        for i in range(max(x.bit_length(),y.bit_length())):
            if (x & (1<<i)) ^ (y & (1<<i)):
                res += 1
        return res