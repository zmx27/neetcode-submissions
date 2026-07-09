class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[1,0], [-1,0], [0, 1], [0,-1]]

        # Traverse connected "O" cells and mark them as visited
        def dfs(r, c):
            if min(r,c) < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            
            board[r][c] = "#"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr,nc)

        # Traverse for cells in left and right border
        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][COLS-1] == "O":
                dfs(r, COLS-1)
        
        # Traverse for cells in top and bottom border
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROWS-1][c] == "O":
                dfs(ROWS-1, c)
        
        # Traverse the grid again
        # Unmark "#" back to "O"
        # Capture the "O" as "X"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "#":
                    board[r][c] = "O"

        