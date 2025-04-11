# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)

        for start,end in (edges):
            graph[end].append(start)
        def dfs(node):
            if node not in visited:
                my_ancestor.append(node)
            visited.add(node)
            for parent in graph[node]:
                if parent not in visited:
                    # my_ancestor.append(parent)
                    dfs(parent)


        ancestor = [[]for i in range(n)]
        for i in range(n):
            my_ancestor = list()
            visited = {i}
            dfs(i)
            ancestor[i] = sorted(my_ancestor)
        return ancestor
        