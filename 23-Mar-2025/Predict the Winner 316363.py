# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def back(nums,turn):
            if len(nums) == 1:
                if turn:
                    return nums[0]
                else:
                    return -nums[0]


            if turn:
                first = back(nums[1:],not turn) + nums[0]
                second = nums[-1] + back(nums[:-1],not turn)
                return max(first,second)

            else: 
                first = back(nums[1:],not turn) - nums[0]
                second =  back(nums[:-1],not turn) - nums[-1] 

                return min(second,first)

            
           
            
           
            


        res = back(nums,True)
        # print(res)
        if res >=0:
            return True
        else:
            return False
                       
        