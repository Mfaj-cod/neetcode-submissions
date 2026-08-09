class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prevHeight):
            if ((r, c) in visited or r < 0 or c < 0 or r==ROWS or c==COLS or heights[r][c] < prevHeight):
                return
            
            visited.add((r, c))
            dfs(r, c, visited, heights[r][c])
            dfs(r, c, visited, heights[r][c])


        for c in range(COLS):
            dfs(0, c, pacific, heights[r][c])
            dfs(ROWS-1, c, atlantic, heights[ROWS-1][c])
