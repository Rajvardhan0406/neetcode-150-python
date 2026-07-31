from collections import deque
from typing import List

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [[] for _ in range(n)]

        for i in range(n):
            xi, yi, ri = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                xj, yj, _ = bombs[j]
                dist_sq = (xi - xj) ** 2 + (yi - yj) ** 2
                if dist_sq <= ri * ri:
                    graph[i].append(j)

        def bfs(start):
            visited = {start}
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return len(visited)

        max_detonated = 0
        for i in range(n):
            max_detonated = max(max_detonated, bfs(i))

        return max_detonated