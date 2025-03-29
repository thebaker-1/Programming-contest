# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        def valid(max_i):
            prefix = [0]*(len(nums)+1)
            for i in range(max_i):
                left_most,right_most,add = queries[i]
                prefix[left_most] += add
                prefix[right_most + 1] -= add
            
            for i in range(1,len(nums)):
                prefix[i] += prefix[i-1]

            for i in range(len(nums)):
                if prefix[i] < nums[i]:
                    return False
            return True

        l = 0
        r = len(queries)
        ans = -1

        while l <= r:
            mid = (l+r)//2
            if valid(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
