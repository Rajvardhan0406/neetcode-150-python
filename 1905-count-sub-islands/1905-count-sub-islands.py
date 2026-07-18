from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid2), len(grid2[0])
        
        def dfs(row: int, col: int) -> bool:
            if row < 0 or row >= m or col < 0 or col >= n or grid2[row][col] == 0:
                return True 
            
            grid2[row][col] = 0
            
            is_valid = (grid1[row][col] == 1)
            
            
            up = dfs(row - 1, col)
            down = dfs(row + 1, col)
            left = dfs(row, col - 1)
            right = dfs(row, col + 1)
            
            return is_valid and up and down and left and right
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        count += 1
        
        return count