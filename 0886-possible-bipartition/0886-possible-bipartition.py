from collections import deque, defaultdict
from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        color = {}  

        for person in range(1, n + 1):
            if person in color:
                continue
            color[person] = 0
            queue = deque([person])
            while queue:
                cur = queue.popleft()
                for nei in graph[cur]:
                    if nei not in color:
                        color[nei] = 1 - color[cur]
                        queue.append(nei)
                    elif color[nei] == color[cur]:
                        return False

        return True