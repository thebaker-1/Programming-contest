# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for u,v in prerequisites:
            graph[v].append(u)
        
        def dfs(node):

            color[node] = 1
            for nei in graph[node]:
                if color[nei] == 1:
                    return False
                elif color[nei] == 0:
                    if not dfs(nei):
                        return False
            res.append(node)
            color[nei] = 2

            return True         

        color = defaultdict(list)
        res = []
        for i in range(numCourses):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return []
        return res[::-1]




            


        