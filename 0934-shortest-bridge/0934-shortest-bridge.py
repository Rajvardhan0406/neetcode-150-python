class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        n = len(grid)
        from collections import deque
        
        def get_neighbors(r, c):
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    yield nr, nc
        
        visited = [[False]*n for _ in range(n)]
        queue = deque()
        
        def dfs(r, c):
            stack = [(r, c)]
            visited[r][c] = True
            while stack:
                cr, cc = stack.pop()
                queue.append((cr, cc, 0))
                for nr, nc in get_neighbors(cr, cc):
                    if not visited[nr][nc] and grid[nr][nc] == 1:
                        visited[nr][nc] = True
                        stack.append((nr, nc))
        
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break
        
        while queue:
            r, c, dist = queue.popleft()
            for nr, nc in get_neighbors(r, c):
                if visited[nr][nc]:
                    continue
                if grid[nr][nc] == 1:
                    return dist 
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))
        
        return -1  