# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(l,r):
            nonlocal res
            mid = (l+r)//2
            if l > r:
                return
            if nums[mid] == target:
                res = mid
                return 
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
            binary(l,r)
        res = -1
        binary(0,len(nums)-1)
        return res
        