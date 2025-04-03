# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0 
        res = []
        while i < len(nums):
            if nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1],nums[i] = nums[i], nums[nums[i]-1]
            else:
                i += 1
        idx = 0
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(nums[i])
        
        return res

        