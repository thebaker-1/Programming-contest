# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        mat = isWater
        rows,cols = len(mat),len(mat[0])
        q = deque()
        visited = set()
        for row in range(rows):
            for col in range(cols):
                if mat[row][col]:
                    mat[row][col] = 0
                    q.append([row,col])
                    visited.add((row,col))
        while q:
            row,col = q.popleft()
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for ro,co in directions:
                r = row +ro
                c = col +co
                if ((r,c) not in visited and -1<r<rows and -1<c<cols):
                    mat[r][c] = mat[row][col] + 1
                    visited.add((r,c))
                    q.append([r,c])
        return mat        