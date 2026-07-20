from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n 

        for start in range(n):
            if color[start] != -1:
                continue
            color[start] = 0
            queue = deque([start])
            while queue:
                cur = queue.popleft()
                for nei in graph[cur]:
                    if color[nei] == -1:
                        color[nei] = 1 - color[cur]
                        queue.append(nei)
                    elif color[nei] == color[cur]:
                        return False

        return True