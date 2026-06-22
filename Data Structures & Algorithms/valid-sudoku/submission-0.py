class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set) # cols[c] tracks seen ints in column c
        rows = defaultdict(set) # rows[r] tracks seen ints in row r
        square = defaultdict(set) # square[(r,c)] tracks ints seen in square (r//3, c//3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in cols[c] or val in rows[r] or val in square[(r//3, c//3)]:
                    return False
                cols[c].add(val)
                rows[r].add(val)
                square[(r//3, c//3)].add(val)
        
        return True
                