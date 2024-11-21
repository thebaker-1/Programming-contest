class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        found = set()
        i = 0
        for j in range(len(nums)):
            if j-i > k:
                found.discard(nums[i])
                i+=1
            if nums[j] not in found:
                found.add(nums[j])
            else:
                return True
        return False
            
        