# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        new_board = []
        reverse = False
        for i in range(len(board)-1,-1,-1):
            if not reverse:
                new_board.extend(board[i])
            else:
                new_board.extend(board[i][::-1])
            reverse = not reverse
        start = 0
        q = deque([0])
        visited = {0}
        step = -1
        directions = [1,2,3,4,5,6]
        while q:
            step += 1
            for _ in range(len(q)):
                i = q.popleft()
                if i == len(new_board) - 1:
                    return step
                visited.add(i)

                for go in directions:
                    new_pos = min(len(new_board)-1,go + i)
                    if new_board[new_pos] != -1:
                        new_pos = new_board[new_pos] - 1
                    if new_pos not in visited:
                        q.append(new_pos)
                        visited.add(new_pos)
        return -1 
