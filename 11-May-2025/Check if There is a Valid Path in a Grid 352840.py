# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)] 
        self.size = [1 for i in range(size)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parx = self.find(x)
        pary = self.find(y)
        if parx != pary:
            if self.size[parx] >= self.size[pary]:
                self.parent[pary] = parx
                self.size[parx] += self.size[pary]
            else:
                self.parent[parx] = pary
                self.size[pary]  += self.size[parx]

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        if len(grid) == 1 and len(grid[0]) == 1:
            return True

        STREET_CONNECTIONS = {
            1: ['left', 'right'],
            2: ['up', 'down'],
            3: ['left', 'down'],
            4: ['right', 'down'],
            5: ['left', 'up'],
            6: ['right', 'up'],
        }
        rows, cols = len(grid), len(grid[0])
        uf = UnionFind(rows * cols)

        def grid_no(i, j):
            return i * cols + j
        uf = UnionFind((max(rows, cols)+ 1 )**2)
        def grid_no(i,j):
            return i*cols + j

        for i in range(rows):
            for j in range(1,cols):  
                possible  = 'left' in STREET_CONNECTIONS[grid[i][j]] and "right" in STREET_CONNECTIONS[grid[i][j-1]]            
                if possible:
                    uf.union(grid_no(i,j),grid_no(i,j-1))
        for j in range(cols):
            for i in range(1,rows):
                possible  = 'up' in STREET_CONNECTIONS[grid[i][j]] and "down" in STREET_CONNECTIONS[grid[i-1][j]]   
                if possible:
                    uf.union(grid_no(i,j),grid_no(i-1,j))
        
        return  uf.find(0) == uf.find(rows*cols - 1)
