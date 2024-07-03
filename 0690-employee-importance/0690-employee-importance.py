"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        l = defaultdict(list)
        for em in employees:
            l[em.id].append([em.importance,em.subordinates])
        self.res = 0
        def dfs(graph):
            self.res +=graph[0][0]
            if not graph[0][1]:
                return
            for child_id in graph[0][1]:
                dfs(l[child_id])
        dfs(l[id])
        return self.res

            
        