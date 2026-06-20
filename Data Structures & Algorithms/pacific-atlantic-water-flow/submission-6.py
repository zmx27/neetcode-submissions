class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1,0), (-1, 0), (0, -1), (0, 1)]

        def dfs(r, c, ocean, prev):
            if (r,c) in ocean or min(r,c) < 0 or r == ROWS or c == COLS or heights[r][c] < prev:
                return
            
            ocean.add((r,c))
            for dr, dc in directions:
                dfs(r+dr, c+dc, ocean, heights[r][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        
        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        return res