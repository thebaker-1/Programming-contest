# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # this approach try to find the farthest node from the first node (note that the first node does not garanted to be the longest path but we could find the longest path from that node then since that node is the last node)
        # then we will get the longest node from the last node  
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[v] += 1
            indegree[u] += 1
        
        q = deque()

        for i in range(n):
            if indegree[i] <= 1:
                q.append(i)
        visited = set()
        if 1<= len(q) <= 2:
            lastq = [i for i in q]

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                visited.add(node)
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if nei not in visited and indegree[nei] == 1:
                        q.append(nei)
            if 1 <= len(q) <= 2:
                lastq = [i for i in q]
            
        return lastq
