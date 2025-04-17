# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        high = max(candies)
        low = 0

        def valid(mid):
            if not mid: return True
            count = 0
            for i in range(len(candies)):
                count += candies[i]//mid
            return count >= k

        while low <= high:
            mid = (low + high) // 2
            if valid(mid):
                low = mid + 1
            else:
                high = mid - 1
        return low - 1