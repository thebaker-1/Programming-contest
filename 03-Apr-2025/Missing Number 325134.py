# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        i = 0
        while i < len(nums):
            correct = nums[i]
            if nums[i] != i and nums[i] != len(nums):
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i:
                return i
                
        return len(nums)