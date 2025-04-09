# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        satisfy = set()
        for i in range(n):
            satisfy.add(i)
        
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
        
        for neis in graph.values():
            for nei in neis:
                satisfy.discard(nei)
        if len(satisfy) == 1:
            return next(iter(satisfy))
        return -1

        