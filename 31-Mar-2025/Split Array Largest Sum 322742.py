# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def valid(sums):

            part_sum = 0
            partitions = 1
            for i in range(len(nums)):
                if part_sum + nums[i] > sums:
                    part_sum = 0
                    partitions += 1
                if part_sum + nums[i] <= sums:
                    part_sum += nums[i]
            return partitions <= k
    
        l = max(nums)
        r = sum(nums)
        count  = 0
        while l <= r:

            mid = (l+r)//2
            if  valid(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l
        