# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def back(i,store,check):
            nonlocal n
            if len(store) == n:
                res.append(store[:])
                return 
            for j in range(n):
                if nums[j] not in check:
                    store.append(nums[j])
                    check.add(nums[j])
                    back(j,store,check)
                    store.pop()
                    check.discard(nums[j])
        back(0,[],set())
        return res

