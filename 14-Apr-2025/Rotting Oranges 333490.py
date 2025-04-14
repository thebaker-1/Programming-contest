# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i,j])
                elif grid[i][j] == 1:
                    fresh += 1
        visited = set()
        time = 0
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        while q:
            if fresh < 1:
                break
            time += 1

            for _ in range(len(q)):
                i,j = q.popleft()

                for r,c in [[0,1],[0,-1],[1,0],[-1,0]]:
                    row = r + i
                    col = c + j
                    if inbound(row,col) and grid[row][col] == 1:
                        fresh -= 1
                        grid[row][col] = 2
                        q.append([row,col])
            
        if fresh > 0:
            return -1
        return time
        