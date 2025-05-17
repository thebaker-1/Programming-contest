# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        last_same = left
        new_num = 0
        for i in range(32,-1,-1):
            if left & (1 << i) ^ (right & (1 << i)):
                last_same = i
                break
            new_num |= left & (1 << i)
        return new_num
        
        