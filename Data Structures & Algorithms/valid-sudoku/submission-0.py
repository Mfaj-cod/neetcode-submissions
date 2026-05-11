class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])

        for i in range(row):
            row_set = set()
            for j in board[i]:
                if j == ".":
                    continue
                elif j in row_set:
                    return False
                row_set.add(j)

        for i in range(col):
            col_set = set()
            for j in range(col):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in col_set:
                    return False
                col_set.add(board[j][i])

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                sq_set = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        val = board[i][j]
                        if val == ".": 
                            continue
                        if val in sq_set:
                            return False
                        sq_set.add(val)
        
        return True
