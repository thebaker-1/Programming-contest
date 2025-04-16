# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row, col):
            return (0 <= row < len(mat) and 0 <= col < len(mat[0]))

        near0 = [[-1]* len(mat[0]) for i in range(len(mat))]
        q = deque()

        visited = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
        add = -1
        while q:
            add += 1
            length = len(q)
            for _ in range(length):
                i,j = q.popleft()
                near0[i][j] = add
                visited.add((i,j))
                for r,c in directions:
                    row = r + i
                    col = c + j
                    if inbound(row,col) and (row,col) not in visited:
                        visited.add((row,col))
                        q.append((row,col))
            
        return near0
            

        