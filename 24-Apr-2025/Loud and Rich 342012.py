# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        indegree = defaultdict(int)
        graph = defaultdict(list)
        for u,v in richer:
            graph[v].append(u)
            indegree[u] += 1
        
        def dfs(person):
            visited.add(person)
            if person not in graph:
                return 
            for poor in graph[person]:
                if poor not in visited:
                    dfs(poor)
                if quiet[res[person]] > quiet[res[poor]]:
                    res[person] = res[poor]

        n = len(quiet)
        res =  [i for i in range(n)]
        visited = set()
        for i in range(n):
            if i not in indegree:
                dfs(i)

        return res

        