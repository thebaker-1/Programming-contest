# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        def valid(mid):
            count = 1
            total = 0
            for i in range(len(weights)):
                if total + weights[i] > mid:
                    total = 0
                    count += 1
                total += weights[i]
            return count <= days

        while l <= r:
            mid = (l + r)//2
            if valid(mid):
                r = mid - 1
            else:
                l = mid + 1
        return r + 1
        