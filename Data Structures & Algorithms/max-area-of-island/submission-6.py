class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0 # track max area
        visited = set() # dont visit same cell again to avoid infinite recursion

        def dfs(r, c):
            if min(r,c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r,c) in visited:
                return 0 # base case
            
            directions = [[1,0], [-1,0], [0, 1], [0,-1]]
            area = 1 # count the current cell
            visited.add((r,c))
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                area += dfs(newR, newC) # accumulate the area
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    # Start dfs on a non visited island cell
                    maxArea = max(maxArea, dfs(r,c))
        
        return maxArea
