# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        bad = -1
        i = 0
        j = 0
        recentmin = -1
        recentmax = -1
        count = 0
        while j < len(nums):
            if nums[j] == minK:
                recentmin = j
            if nums[j] == maxK:
                recentmax = j
            # invalid window
            if nums[j] < minK or nums[j] > maxK:
                bad = j
            # valid window
            elif recentmin != -1 and recentmax != -1 and min(recentmin,recentmax) > bad:
                count += min(recentmin,recentmax) - bad
            j += 1
        return count

