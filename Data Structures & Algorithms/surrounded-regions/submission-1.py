class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def onEdge(r, c):
            if r == ROWS-1 or r == 0 or c == COLS-1 or c == 0:
                return True
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if not onEdge(r, c) and board[r][c]=="O":
                    board[r][c] = "X"
        