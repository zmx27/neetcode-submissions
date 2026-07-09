class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        area = 0

        def bfs(r,c):
            q = deque()
            res = 1
            q.append((r,c))
            grid[r][c] = 0

            while q:
                oldR, oldC = q.popleft()
                for dr, dc in directions:
                    newR, newC = oldR + dr, oldC + dc
                    if min(newR, newC) < 0 or newR == ROWS or newC == COLS or grid[newR][newC] == 0:
                        continue
                    q.append((newR,newC))
                    grid[newR][newC] = 0
                    res += 1
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, bfs(r,c))
        return area