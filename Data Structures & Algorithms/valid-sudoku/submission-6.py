class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        rows = defaultdict(set)
        square = defaultdict(set)

        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == ".":
                    continue
                if board[row][column] in col[column] or board[row][column] in rows[row] or board[row][column] in square[(row // 3, column // 3 )]:
                    return False
                rows[row].add(board[row][column])
                col[column].add(board[row][column])
                square[(row // 3, column // 3 )].add(board[row][column])
        return True



        