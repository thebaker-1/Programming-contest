# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] and i != j:
                    graph[i].append(j)

        def dfs(i):
            visited.add(i)
            for nei in graph[i]:
                if nei not in visited:
                    dfs(nei)

        visited = set()
        count = 0
        for i in range(len(isConnected)):
            if i not in visited:
                count += 1
                dfs(i)
        return count

        
        