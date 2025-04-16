# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a,b in ((redEdges)):
            graph[a].append((b,True))
        for u,v in ((blueEdges)):
            graph[u].append((v,False))


        res = [-1]*(n)
        # start with red
        q = deque()
        q.append((0,True))
        visited = set()
        level = -1
        while q:
            length = len(q)
            level += 1
            for _ in range(length):
                node,color = q.popleft()
                visited.add((node,color))
                if res[node] == -1 or res[node] > level:
                    res[node] = level
                for nei, c in graph[node]:
                    if c != color and (nei,c) not in visited:
                        visited.add((nei,c))
                        q.append((nei,not color))
        # start with blue
        q = deque()
        q.append((0,False))
        visited = set()
        level = -1
        while q:
            length = len(q)
            level += 1
            for _ in range(length):
                node,color = q.popleft()
                visited.add((node,color))
                if res[node] == -1 or res[node] > level:
                    res[node] = level
                for nei, c in graph[node]:
                    if c != color and (nei,c) not in visited:
                        visited.add((nei,c))
                        q.append((nei,not color))
        return res
        
                    

        

        