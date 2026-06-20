class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        
        def dfs(r, c):
            if min(r,c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            for dx in directions:
                dfs(r + dx[0], c + dx[1])
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        return islands

        