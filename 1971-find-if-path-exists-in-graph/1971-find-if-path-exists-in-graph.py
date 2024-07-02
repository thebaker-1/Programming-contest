class Solution:
    def validPath(self, n, edges,source, destination):
        graph = defaultdict(list)
        for start,end in edges:
            graph[start].append(end)
            graph[end].append(start)
        # dfs traversal using stack
        stack =  [source]
        seen = set()
        seen.add(source)
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    stack.append(nei)
        return False




        