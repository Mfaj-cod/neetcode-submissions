class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def onEdge(r, c):
            if r == ROWS-1 or r == 0 or c == COLS-1 or c == 0:
                return True
            return False
        
        for r in range(1, ROWS-1):
            for c in range(1, COLS-1):
                board[r][c] = "X"
        