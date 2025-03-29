# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        def valid(h_index):
            i = len(citations) - h_index 
            if h_index == 0:
                return True

            return citations[i] >= h_index

        l = 0
        r = len(citations)

        while l <= r:
            mid = (l+r)//2
            # print(mid) 
            if valid(mid):
                l = mid + 1
            else:
                r = mid - 1
                
        return r 
        