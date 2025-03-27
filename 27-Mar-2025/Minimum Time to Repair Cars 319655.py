# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def valid(time):
            carleft = cars
            for rank in ranks:
                x = 0
                x = floor(math.sqrt(time/rank) )
                # for car in range(0,cars+1):
                #     if car * car > time/rank:
                #         break
                #     x = car
                carleft -= x
                if carleft <= 0:
                    return True
            return False

        l = 0
        r = min(ranks) * pow(cars,2)
        while l <= r:
            mid = (l+r)//2
            if valid(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
        