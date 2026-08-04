class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        # prefix sum matrix padded with an extra row and column of 0s
        self.prefix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        # Build the 2D prefix sums
        for r in range(ROWS):
            for c in range(COLS):
                self.prefix[r + 1][c + 1] = (
                    matrix[r][c] + 
                    self.prefix[r][c + 1] + 
                    self.prefix[r + 1][c] - 
                    self.prefix[r][c]
                )


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Calculate the target rectangle using Inclusion-Exclusion
        # adding 1 to all coordinates to align with our padded prefix matrix
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        
        return (
            self.prefix[row2][col2] - 
            self.prefix[row1 - 1][col2] - 
            self.prefix[row2][col1 - 1] + 
            self.prefix[row1 - 1][col1 - 1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)