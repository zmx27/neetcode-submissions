class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # Treat the matrix as one large sorted array
        l, r = 0, ROWS * COLS - 1
        while (l <= r):
            m = (l + r) // 2
            # Convert this mid value into a row, col equivalent
            row, col = m // COLS, m % COLS
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = m + 1
            else:
                r = m - 1
        return False