# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def inbound(i,j):
            return 0 <= i < len(board) and 0 <= j < len(board[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(i,j):
            nonlocal valid
            visited.add((i,j))
            for r,c in directions:
                row = r + i
                col = c + j
                if not inbound(row,col):
                    valid = False
                elif board[row][col] == "O" and (row,col) not in visited:
                    island.append((row,col))
                    dfs(row,col)          
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i,j) not in visited:
                    island = []
                    island.append((i,j))
                    valid = True
                    dfs(i,j)
                    if valid:
                        for ro,co in island:
                            board[ro][co] = "X"
                        
        