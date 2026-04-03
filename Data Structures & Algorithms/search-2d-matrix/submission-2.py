class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLUMN = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLUMN - 1

        while l <= r:
            mid = l + (r - l) // 2
            row = mid // COLUMN
            column = mid % COLUMN

            if target > matrix[row][column]:
                l = mid + 1
            elif target < matrix[row][column]:
                r = mid - 1
            else:
                return True
        return False