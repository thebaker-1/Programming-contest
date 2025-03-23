# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = set()
        def backtrack(i,store):
            if i == n:
                res.add("".join(store[:]))
                return
            for j in ["0","1"]:
                if not store or store[-1] == "1" or j == "1":
                    store.append(j)
                    backtrack(i+1,store)
                    store.pop()
        backtrack(0,[])
        return list(res)
                