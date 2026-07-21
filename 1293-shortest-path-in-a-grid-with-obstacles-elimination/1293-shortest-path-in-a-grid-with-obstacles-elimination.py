from typing import List
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

       
        if k >= m + n - 2:
            return m + n - 2

        visited = [[-1] * n for _ in range(m)]
        visited[0][0] = k

        queue = deque([(0, 0, k, 0)]) 
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            row, col, k_left, dist = queue.popleft()

            if row == m - 1 and col == n - 1:
                return dist

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_k = k_left - grid[nr][nc] 
                    if new_k >= 0 and new_k > visited[nr][nc]:
                        visited[nr][nc] = new_k
                        queue.append((nr, nc, new_k, dist + 1))

        return -1