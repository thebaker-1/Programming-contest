# Problem: Number of Subsequences That Satisfy the Given Sum Condition - https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        i, j = 0, len(nums)-1
        count = 0

        while i <= j:
            if nums[i] + nums[j] <= target:
                count += (2**(j-i)) % (10**9+7)
                i += 1
            else:
                j -= 1
        return count % (10**9+7)
