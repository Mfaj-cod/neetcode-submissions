class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        minheap = [[0, 0, 0]] # [diff, r, c]
        visited = set()

        while minheap:
            diff, r, c = heapq.heappop(minheap)
            if (r, c) in visited:
                continue
            visited.add((r, c))

            if r == ROWS - 1 and c == COLS - 1:
                return diff
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS) or (nr, nc) in visited:
                    continue

                newdiff = max(diff, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(minheap, [newdiff, nr, nc])

