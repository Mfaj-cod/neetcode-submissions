class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(i, c, r):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path):
                return False
            
            path.add((r, c))
            res = (dfs(i+1, c, r+1) or
                   dfs(i+1, c, r-1) or
                   dfs(i+1, c+1, r) or
                   dfs(i+1, c-1, r))

            path.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, c, r): return True

        return False

        # O(n * m * 4^n)
