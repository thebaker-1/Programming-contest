# Problem: Find Xor-Beauty of Array - https://leetcode.com/problems/find-xor-beauty-of-array/

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        length = max(nums).bit_length()
        binary = []
        for bit_i in range(length):
            bits = defaultdict(int)
            for num in nums:
                if num & (1<<bit_i):
                    bits[1] += 1
                else:
                    bits[0] += 1
            total = (bits[0] + bits[1])**2
            count_0 = bits[0]**2
            count_1 = total - count_0
            if count_1 & (1):
                binary.append("1")
            else:
                binary.append("0")

        return int("".join(binary[::-1]),2)

                 

