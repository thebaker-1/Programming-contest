# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if image[sr][sc] == color: return image
        def inbound(row,col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])

        compare = image[sr][sc]
        start = (sr,sc)
        q = deque()
        q.append(start)
        visited = set()
        visited.add(start)
        while q:
            n = len(q)
            for _ in range(n):
                i,j = q.popleft()
                visited.add((i,j))
                for r,c in [(0,1),(0,-1),(1,0),(-1,0)]:
                    row = r + i
                    col = c + j
                    if inbound(row,col) and image[row][col] == compare and (row,col) not in visited:
                        visited.add((row,col))
                        q.append((row,col))
        changed_pixel = [[image[i][j] for j in range(len(image[0]))]for i in range(len(image))]
        for i,j in visited:
            changed_pixel[i][j] = color
        return changed_pixel
        