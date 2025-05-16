# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        store = 0
        max_len = 0
        i = 0
        for j in range(len(nums)):
            tf = True
            while store & nums[j] != 0 and i < len(nums):
                tf = False
                store ^= nums[i]
                i += 1
            store |= nums[j]
            max_len = max(max_len, j - i + 1)

        return max_len
            

