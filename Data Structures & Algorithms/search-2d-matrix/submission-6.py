class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLUMNS = len(matrix), len(matrix[0])

        #Same pattern
        l, r = 0, ROWS * COLUMNS - 1

        while l <= r:
            m = l + (r - l) // 2

            row = m // COLUMNS
            col = m % COLUMNS

            if (matrix[row][col] == target):
                return True
            elif matrix[row][col] > target:
                r = m - 1
            else:
                l = m + 1
        return False


        