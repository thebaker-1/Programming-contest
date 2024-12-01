class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = 0
        for j in range(m,len(nums1)):
            nums1[j]=nums2[i]
            i+=1
        nums1.sort()


        