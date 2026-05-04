class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        low, high = 0, (rows * cols) - 1

        while low <= high:
            mid = (low + high) // 2
            
            # Map the 1D index back to 2D coordinates (row, col)
            # row = index // width
            # col = index % width
            mid_val = matrix[mid // cols][mid % cols]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False