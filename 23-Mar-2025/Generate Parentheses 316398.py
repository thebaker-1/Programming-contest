# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()
        def backtrack(store,opened,closed):
            if len(store) == n * 2:
                if opened == closed:
                    res.add("".join(store[:]))
                return 
            for j in ["(",")"]:
                if j == "(":
                    store.append(j)
                    backtrack(store,opened+1,closed)
                    store.pop()
                elif opened > closed:
                    store.append(j)
                    backtrack(store,opened,closed+1)
                    store.pop()
        backtrack([],0,0)
        return list(res)
        