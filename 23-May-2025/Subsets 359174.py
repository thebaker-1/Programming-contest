# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        print(res)
        for num in range((2**len(nums))):
            half = []
            for i in range(len(nums)):
                if num & (1 << i):
                    half.append(nums[i])
            res.append(half)
        return res



        