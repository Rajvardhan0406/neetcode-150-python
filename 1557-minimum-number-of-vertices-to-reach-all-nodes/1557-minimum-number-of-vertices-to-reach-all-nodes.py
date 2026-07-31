from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = [0] * n

        for _, to in edges:
            in_degree[to] += 1

        return [node for node in range(n) if in_degree[node] == 0]