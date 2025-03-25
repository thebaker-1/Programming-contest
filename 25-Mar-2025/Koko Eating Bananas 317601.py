# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        l = 1
        r = max(piles)
        while l <= r:
            mid = (l + r)//2
            count = 0
            for i in range(len(piles)):
                count += (ceil(piles[i]/mid))
            if count <= h:
                r = mid - 1
            else:
                l = mid + 1
        return l
