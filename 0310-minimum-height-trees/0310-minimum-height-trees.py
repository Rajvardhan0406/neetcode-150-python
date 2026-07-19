from typing import List
from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        leaves = deque([node for node in range(n) if len(graph[node]) == 1])
        remaining_nodes = n

        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count

            for _ in range(leaves_count):
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    graph[neighbor].remove(leaf)
                    if len(graph[neighbor]) == 1:
                        leaves.append(neighbor)

        return list(leaves)