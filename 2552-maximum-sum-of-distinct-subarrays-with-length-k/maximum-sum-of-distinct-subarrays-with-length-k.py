class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = float("-inf")
        cur_sum = 0
        max_unique_value = 0
        i = 0
        unique = defaultdict(int)
        for j in range(len(nums)):
            cur_sum += nums[j]
            unique[nums[j]]+=1
            max_unique_value = max(max_unique_value,unique[nums[j]])
            if j-i+1 >=k:
                if max_unique_value ==1:
                    max_sum = max(max_sum,cur_sum)
                cur_sum-=nums[i]
                if unique[nums[i]] == 1:
                    unique.pop(nums[i])
                else:
                    unique[nums[i]]-=1
                    max_unique_value = max(unique.values())
                i+=1
        
        return max_sum if max_sum != float("-inf") else 0

            
        