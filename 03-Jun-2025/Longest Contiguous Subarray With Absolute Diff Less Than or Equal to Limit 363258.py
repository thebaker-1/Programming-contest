# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        smallest = deque()
        largest = deque()
        mini = 0 
        max_size = 0
        for idx, num in enumerate(nums):
            while smallest and nums[smallest[-1]] >= num:
                smallest.pop()
            smallest.append(idx)
            while largest and nums[largest[-1]] <= num:
                largest.pop()
            largest.append(idx)

            while nums[largest[0]] - nums[smallest[0]] > limit:
                mini += 1
                if largest[0] < mini:
                    largest.popleft()
                if smallest[0] < mini:
                    smallest.popleft()

            max_size = max(max_size, idx - mini + 1)

        return max_size
        