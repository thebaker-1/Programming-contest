class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        curr = 0 
        for i in range(len(nums)):
            curr += nums[i]
            if  curr - nums[i]== total - curr:
                return i
        return -1
        