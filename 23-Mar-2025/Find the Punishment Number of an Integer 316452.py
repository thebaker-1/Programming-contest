# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:

        def check_valid(i,store,sums):
            nonlocal valid
            if i == len(square):
                if sums == sqrt(int(square)):
                    valid = True
                return 
            for j in range(i,len(square)):
                store.append(square[i:j+1])
                sums += int(square[i:j+1])
                check_valid(j+1,store, sums)
                sums -= int(square[i:j+1])
                store.pop()
                if valid:
                    break

        res = 0
        for i in range(1,n+1):
            square = str(i*i)
            square_int = i*i
            valid = False
            check_valid(0,[],0)
            if valid:
                res += square_int

        return res