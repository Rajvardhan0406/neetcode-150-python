from typing import List
from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0

        full_mask = (1 << n) - 1
        queue = deque()
        visited = set()

        for i in range(n):
            state = (i, 1 << i)
            queue.append((i, 1 << i, 0))  
            visited.add(state)

        while queue:
            node, mask, dist = queue.popleft()

            if mask == full_mask:
                return dist

            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)
                new_state = (neighbor, new_mask)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((neighbor, new_mask, dist + 1))

        return -1 