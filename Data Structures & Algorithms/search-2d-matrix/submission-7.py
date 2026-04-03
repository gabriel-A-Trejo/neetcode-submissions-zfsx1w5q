class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLUMNS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLUMNS - 1

        while l <= r:
            mid = l + (r - l) // 2
            row, col = mid // COLUMNS,  mid % COLUMNS
            if matrix[row][col] < target:
                l += 1
            elif matrix[row][col] > target:
                r -= 1
            else: return True
        return False
            

        