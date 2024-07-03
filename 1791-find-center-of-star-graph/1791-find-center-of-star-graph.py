class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for e,v in edges:
            graph[e].append(v)
            graph[v].append(e)
        for i in graph:
            if (len(graph[i])) >= len(graph)-1:
                return i
