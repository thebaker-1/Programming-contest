# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        indegree = defaultdict(int)
        ngraph = defaultdict(list)
        for u in range(len(graph)):
            for v in graph[u]:
                ngraph[v].append(u)
                indegree[u] += 1

        q = deque()
        res = []
        for i in range(len(graph)):
            if not indegree[i]:
                q.append(i)
                res.append(i)

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for nei in ngraph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] < 1:
                        q.append(nei)
                        res.append(nei)
        return sorted(res)



