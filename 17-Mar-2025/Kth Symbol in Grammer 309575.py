# Problem: Kth Symbol in Grammer - https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def rec(k):
            if k == 1:
                return False
            if k % 2:
                return rec(math.ceil(k/2))
            else:
                return not rec(math.ceil(k/2))
        return 1 if rec(k) else 0