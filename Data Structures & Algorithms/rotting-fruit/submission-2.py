class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        minutes, fresh_fruits = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    q.append((r, c))
                elif grid[r][c]==1:
                    fresh_fruits += 1
        
        def bfs(r: int, c: int) -> None:
            nonlocal fresh_fruits
            
            for dr, dc in directions:
                nr, nc = r + dr, c +  dc
                if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc]==1:
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh_fruits -= 1

        while q and fresh_fruits > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                bfs(r, c)
            minutes += 1
        
        return minutes if fresh_fruits == 0 else -1
