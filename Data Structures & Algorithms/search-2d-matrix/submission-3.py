class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Plan:
        first lets get the row and column: row will be the length and column will be inside the row
        Two pointers first start 0 and other will be based on Row * column - 1
        while l <= r

        finding the mid point 
            mid = l + (r - l) // 2
            row = mid // COLUMN
            column = mind % COLUMN

            if current mid is bigger then target then will l = mid + 1
            elif current mid is less then target then it will be r = mid - 1
            else return True

        end loop return true

        """

        ROW, COLUMN = len(matrix), len(matrix[0])
        

        l, r = 0, ROW * COLUMN - 1
        while l <= r:
            mid = l + (r - l) // 2
            midRow = mid // COLUMN 
            midColumn = mid % COLUMN

            if matrix[midRow][midColumn] < target:
                l = mid + 1
            elif matrix[midRow][midColumn] > target:
                r = mid - 1
            else:
                return True
        return False