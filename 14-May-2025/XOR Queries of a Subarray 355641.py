# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]

        for i,val in enumerate(arr):
            if i == 0:
                num = 0
            else:
                num = prefix[-1]
            prefix.append(num^val)

        res = []
        for i,j in queries:
            res.append(prefix[i]^prefix[j+1])
        return res