# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            position = nums[i] - 1
            if nums[position] != nums[i]:
                nums[position], nums[i] = nums[i], nums[position]
            else:
                i += 1
        
        res = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(nums[i])
                res.append(i+1)
        return res   