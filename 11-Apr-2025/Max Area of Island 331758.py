# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def valid(ro,co):
            return 0 <= ro < len(grid) and 0 <= co < len(grid[0]) and grid[ro][co] == 1


        def dfs(i,j):
            nonlocal land_count
            if (i,j) in visited or not valid(i,j):
                return 

            land_count += 1
            visited.add((i,j))
            for r,c in [[0,1],[0,-1],[1,0],[-1,0]]:
                row = r + i
                col = c + j
                dfs(row,col)

        visited = set()
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and valid(i,j):
                    land_count = 0
                    dfs(i,j)
                    area = max(area,land_count)
        return area
        