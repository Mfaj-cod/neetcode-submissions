class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):
            peri = 4
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr < ROW and nc < COL and nr >= 0 and nc >= 0 and grid[nr][nc] == 1:
                    peri -= 1
            
            return peri

        perimeter = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    perimeter += bfs(r, c)
        
        return perimeter
