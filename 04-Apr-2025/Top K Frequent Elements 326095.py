# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        res = []
        for i in nums:
            d[i]+=1
        
        for key, value in sorted(d.items(), key=lambda item: item[1],reverse = True):
            res.append(key)
            k-=1
            if k == 0 :
                break
        return res