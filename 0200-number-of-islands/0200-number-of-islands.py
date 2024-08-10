class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visit = set()
        island = 0
        rows ,cols = len(grid),len(grid[0])
        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row,col = q.popleft()
                
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    r = dr + row
                    c =dc + col
                    if -1 < r < rows and -1< c < cols and grid[r][c] =="1" and (r,c) not in visit:
                        visit.add((r,c))
                        q.append((r,c))
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == "1":
                    bfs(r,c)
                    island +=1
        return island