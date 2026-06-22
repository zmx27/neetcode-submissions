class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        q = deque()
        time = 0
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1    

        while q and fresh > 0:
            length = len(q)
            for i in range(length):
                oldR, oldC = q.popleft()
                for dr, dc in directions:
                    newR, newC = oldR+dr, oldC+dc
                    if min(newR, newC) < 0 or newR >= ROWS or newC >= COLS:
                        continue
                    nextPos = grid[newR][newC]
                    if nextPos == 1:
                        grid[newR][newC] = 2
                        q.append((newR, newC))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
