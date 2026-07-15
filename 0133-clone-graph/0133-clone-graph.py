"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}  # original node -> cloned node

        def dfs(orig):
            if orig in visited:
                return visited[orig]

            clone = Node(orig.val)
            visited[orig] = clone

            for neighbor in orig.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)