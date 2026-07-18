from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        WHITE, GRAY, BLACK = 0, 1, 2
        color = [WHITE] * n
        
        def dfs(node: int) -> bool:
            if color[node] == GRAY:
                return False
            if color[node] == BLACK:
                return True
            
            color[node] = GRAY
            
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            
            color[node] = BLACK
            return True
        
        result = []
        for node in range(n):
            if dfs(node):
                result.append(node)
        
        return result