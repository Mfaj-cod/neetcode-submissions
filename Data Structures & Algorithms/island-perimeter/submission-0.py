class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        peri = 0

        def bfs(r: int, c: int) -> int:
            curr = 4
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS and grid[nr][nc] == 1:
                    curr -= 1
            return curr
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    peri += bfs(r, c)
        
        return peri