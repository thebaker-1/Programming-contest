# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for p,c in prerequisites:
            graph[p].append(c)
            indegree[c] += 1
        
        q = deque()
        for i in range(numCourses):
            if i not in indegree:
                q.append(i)

        res = [set() for i in range(numCourses)]
        while q:
            node = q.popleft()

            for child in graph[node]:
                indegree[child] -= 1
                res[child].update(res[node])
                res[child].add(node)
                if indegree[child] == 0:
                    q.append(child)

        ans = []
        for p,c in queries:
            ans.append(p in res[c])
        return ans
            


        