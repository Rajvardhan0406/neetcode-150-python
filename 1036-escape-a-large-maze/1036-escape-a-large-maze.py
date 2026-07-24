from typing import List

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        BOUND = 1_000_000
        blocked_set = {tuple(b) for b in blocked}

      
        k = len(blocked_set)
        limit = k * (k - 1) // 2 if k >= 2 else 0
        
        if limit == 0:
            limit = 1  

        def bfs(start, end):
            visited = {tuple(start)}
            queue = [tuple(start)]
            end = tuple(end)

            while queue:
                if len(visited) > limit:
                    return True  

                next_queue = []
                for x, y in queue:
                    if (x, y) == end:
                        return True
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if (0 <= nx < BOUND and 0 <= ny < BOUND and
                                (nx, ny) not in visited and (nx, ny) not in blocked_set):
                            visited.add((nx, ny))
                            next_queue.append((nx, ny))
                queue = next_queue

            return False  
        if not bfs(source, target):
            return False
        if not bfs(target, source):
            return False

        return True