class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        start = None
        empty = 0  
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] != -1:
                    empty += 1
        
        self.count = 0
        
        def dfs(r, c, steps):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == -1:
                return
            if grid[r][c] == 2:
                if steps == empty - 1:
                    self.count += 1
                return
            
            temp = grid[r][c]
            grid[r][c] = -1  
            steps += 1
            
            dfs(r + 1, c, steps)
            dfs(r - 1, c, steps)
            dfs(r, c + 1, steps)
            dfs(r, c - 1, steps)
            
            grid[r][c] = temp  
        
        dfs(start[0], start[1], 0)
        return self.count