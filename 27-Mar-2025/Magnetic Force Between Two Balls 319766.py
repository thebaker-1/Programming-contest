# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l = 1
        r = position[-1] -  position[0]
        
        def valid(size):
            nonlocal m
            left = 0
            count = 1
            for right in range(len(position)):
                if position[right] - position[left] >= size:
                    count += 1
                    left = right

            return count >= m 


        while l <= r:
            mid = (l+r)//2
            if valid(mid):
                l = mid + 1
            else:
                r = mid - 1
                
        return r
        