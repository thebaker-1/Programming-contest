# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

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
        imp_finder = defaultdict(int)
        graph = defaultdict(list)
        for employee in employees:
            ids = employee.id
            imp = employee.importance
            emp = employee.subordinates
            graph[ids].extend(emp)
            imp_finder[ids] = imp

        def dfs(node):
            nonlocal val
            if node not in visited:
                val += imp_finder[node]
                visited.add(node)
                for emp in graph[node]:
                    if emp not in visited:
                        dfs(emp)
            return val
        visited = set() 
        val = 0
        dfs(id)
        return val
        