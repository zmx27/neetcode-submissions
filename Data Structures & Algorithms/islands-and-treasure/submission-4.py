class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        
        dist = 1
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if min(nr,nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == -1 or (nr,nc) in visited:
                        continue
                    grid[nr][nc] = dist
                    q.append((nr,nc))
                    visited.add((nr,nc))
            dist += 1