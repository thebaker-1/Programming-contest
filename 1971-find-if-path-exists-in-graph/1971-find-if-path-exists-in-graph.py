class Solution:
    def validPath(self, n, edges,source, destination):
        graph = defaultdict(list)
        for start,end in edges:
            graph[start].append(end)
            graph[end].append(start)
        # bfs traversal using queue
        queue = deque()
        queue.append(source)
        seen = set()
        seen.add(source)
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append(nei)
        return False




        