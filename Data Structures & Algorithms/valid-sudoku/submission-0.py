class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set) # key is the columns, and value is the set of number of the column
        rows = defaultdict(set)
        square = defaultdict(set) #key is [r/3, c/3], value is the number

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in square[(r // 3, c // 3)]:
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                square[(r // 3, c // 3)].add(board[r][c])

        return True