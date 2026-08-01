class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """Do not return anything, modify board in-place instead."""

        ROWS, COLS = len(board), len(board[0])

        def onEdge(r, c):
            if (r == ROWS or r < 0 or c == COLS or c < 0) or board[r][c] != "O":
                return
            board[r][c] = "T"
            onEdge(r + 1, c)
            onEdge(r - 1, c)
            onEdge(r, c + 1)
            onEdge(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and r in [0, ROWS-1] or c in [0, COLS-1]:
                    onEdge(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
        
