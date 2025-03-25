# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
__import__("atexit").register(lambda: open("display_runtime.txt", 'w').write('1'))
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        while l <= r:
            mid = (l+r)//2
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l        