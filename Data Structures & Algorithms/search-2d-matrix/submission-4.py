class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Same format as the binary search

        ROWS, COLUMNS = len(matrix), len(matrix[0])

        #Next is use the two pointer method
        l, r = 0, (ROWS * COLUMNS) - 1

        #Same binary search pattern 
        while l <= r:
            mid = (l + r) // 2 
            currRow, currColumn = mid // COLUMNS, mid % COLUMNS

            if target > matrix[currRow][currColumn]:
                l = mid + 1
            elif target < matrix[currRow][currColumn]:
                r = mid - 1
            else:
                return True
        return False


