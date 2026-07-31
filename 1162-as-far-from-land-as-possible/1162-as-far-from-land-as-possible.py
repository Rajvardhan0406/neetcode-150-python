from collections import deque
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))

        if len(queue) == 0 or len(queue) == n * n:
            return -1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        distance = -1
        visited = [[grid[i][j] == 1 for j in range(n)] for i in range(n)]

        while queue:
            distance += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

        return distance