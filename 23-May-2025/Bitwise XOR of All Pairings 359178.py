# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        start1 = 0
        start2 = 0
        if len(nums1) & 1:
            for i in nums2:
                start1 ^= i 
        if len(nums2) & 1:
            for i in nums1:
                start2 ^= i

        return start1 ^ start2
        