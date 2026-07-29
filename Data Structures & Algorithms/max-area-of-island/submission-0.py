class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        def bfs(r: int, c: int) -> int:
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            curr_area = 1

            while q:
                row, col = q.popleft()
                for nr, nc in directions:
                    r, c = row + nr, col + nc

                    if (r in range(ROWS) and c in range(COLS) and grid[r][c]==1 and (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))
                        curr_area += 1

            return curr_area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1 and (r, c) not in visited:
                    curr = bfs(r, c)
                    max_area = max(max_area, curr)
        
        return max_area