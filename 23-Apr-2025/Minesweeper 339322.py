# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        
        def valid(row,col):
            return 0<= row < len(board) and 0<= col < len(board[0])

        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        start = (click[0],click[1])
        q = deque()
        q.append(start)
        visited = set()
        visited.add(start)
        while q:
            length = len(q)
            for _ in range(length):
                i,j = q.popleft()
                visited.add((i,j))

                if board[i][j] == "M":
                    break
                
                visit = set()
                count = 0
                for r,c in directions:
                    row = r + i
                    col = c + j
                    if valid(row,col):
                        if board[row][col] == "M":
                            count += 1
                        elif (row,col) not in visited:
                            visit.add((row,col))

                if not count:
                    board[i][j] = "B"
                    visited.update(visit)
                    for a,b in visit:
                        q.append((a,b))
                else:
                    board[i][j] = str(count)

        return board