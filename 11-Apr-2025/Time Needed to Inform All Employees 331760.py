# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)

        for i in range(len(manager)):
            graph[manager[i]].append([i,informTime[i]])

        def dfs(i,time_i):
            nonlocal total_time
            visited.add(i)
            total_time = max(total_time,time_i)
            if not graph[i]:
                return 0
            for worker,time in graph[i]:
                if worker not in visited:
                    time_i += time
                    dfs(worker,time_i)
                    time_i -= time


        visited = set()
        total_time = 0
        dfs(-1,0)
        return total_time

        