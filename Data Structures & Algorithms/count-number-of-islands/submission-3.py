class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            grid[r][c] = "0"
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr+row, dc+col
                    if (min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0"):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0"


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1
        return islands