class Solution:
    def validPath(self, n, edges,source, destination):
        if source == destination:
            return True
        graph = defaultdict(list)
        for start,end in edges:
            graph[start].append(end)
            graph[end].append(start)
        # bfs traversal using recursion
        seen = []
        def bfs(node,seen):
            if node == destination:
                return True
            for nei in graph[node]:
                if nei not in seen:
                    seen.append(nei)
                    if nei == destination:
                        return True
                    res = bfs(nei,seen)
                    if res:
                        return True
            return False


        return bfs(source,seen)




        