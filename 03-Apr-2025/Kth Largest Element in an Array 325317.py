# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # if k == 50000:
        #     return 1
        def partition(nums):
            piv_i = random.randint(0,len(nums)-1)
            
            pivot = nums[piv_i]
            l = []
            r = []
            for i in range(len(nums)):
                # print(e)
                if i != piv_i:
                    e = random.randint(0,1)
                    if e:
                        if nums[i] > pivot:
                            r.append(nums[i])
                        else:
                            l.append(nums[i])
                    else:
                        if nums[i] >= pivot:
                            r.append(nums[i])
                        else:
                            l.append(nums[i])   
            return l,r,pivot

        k = len(nums) - k + 1
        while len(nums):
            l,r,pivot = partition(nums)

            if len(l) + 1 == k:
                return pivot
            elif len(l) + 1 < k:
                k -= len(l) + 1
                nums = r
            else:
                nums = l
        return -1
            
        

        