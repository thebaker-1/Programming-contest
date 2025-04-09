# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a,b in trust:
            graph[a].add(b)
        satisfy = set()
        for i in range(1,n+1):
            satisfy.add(i)
        for key,value in graph.items():
            satisfy &= value

        if len(satisfy) == 1:
            res = next(iter(satisfy))
            for i in range(1,n+1):
                if i != res and res not in graph[i]:
                    return -1
            return res
        else:
            return -1


        
        