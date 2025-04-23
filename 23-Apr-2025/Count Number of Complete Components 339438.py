# Problem: Count Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
        for i in range(len(graph)):
            graph[i].sort()
        def dfs(node):
            group.add(node)  
            for nei in graph[node]:
                if nei not in group:
                    dfs(nei)
        connected = 0

        visited = set()
        for i in range(n):
            if i not in visited:
                check = set(graph[i]) | set([i])
                valid = True
                group = set()
                dfs(i)
                for child in group:
                    visited.add(child)
                    new_group = set(graph[child]) | set([child])
                    if new_group != check:
                        valid = False
                if valid:
                    connected += 1
        
        return connected
        


        