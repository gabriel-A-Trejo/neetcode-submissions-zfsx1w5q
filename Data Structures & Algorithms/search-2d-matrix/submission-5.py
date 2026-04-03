class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        COLUMN, ROW = len(matrix[0]), len(matrix)
        l, r = 0,  COLUMN * ROW - 1

        while l <= r:
            mid = l + (r - l) // 2
            row = mid // COLUMN
            col = mid % COLUMN

            if  matrix[row][col] == target:
                return  True  
            elif target > matrix[row][col] :
                l = mid + 1
            else:
                r = mid - 1
        return False