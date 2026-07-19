from typing import List
from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        RED, BLUE = 0, 1
        graph = defaultdict(list)

        for a, b in redEdges:
            graph[a].append((b, RED))
        for u, v in blueEdges:
            graph[u].append((v, BLUE))

        visited = set() 
        answer = [-1] * n
        answer[0] = 0

        queue = deque([(0, RED), (0, BLUE)])
        visited.add((0, RED))
        visited.add((0, BLUE))

        steps = 0
        while queue:
            steps += 1
            for _ in range(len(queue)):
                node, last_color = queue.popleft()
                next_color = BLUE if last_color == RED else RED

                for neighbor, edge_color in graph[node]:
                    if edge_color == next_color and (neighbor, edge_color) not in visited:
                        visited.add((neighbor, edge_color))
                        if answer[neighbor] == -1:
                            answer[neighbor] = steps
                        queue.append((neighbor, edge_color))

        return answer