# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        one_count = 0
        mat_row = 0
        for i in range(len(mat)):
            row_one_count = mat[i].count(1)
            if row_one_count > one_count:
                one_count = row_one_count
                mat_row = i
        return [mat_row,one_count]
        