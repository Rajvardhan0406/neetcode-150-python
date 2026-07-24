from collections import deque
from typing import List

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest or not forest[0]:
            return -1

        m, n = len(forest), len(forest[0])
        trees = []
        for r in range(m):
            for c in range(n):
                if forest[r][c] > 1:
                    trees.append((forest[r][c], r, c))
        trees.sort()

        def bfs(start_r, start_c, end_r, end_c):
            if start_r == end_r and start_c == end_c:
                return 0

            visited = [[False] * n for _ in range(m)]
            visited[start_r][start_c] = True
            queue = deque([(start_r, start_c)])
            steps = 0

            while queue:
                steps += 1
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < m and 0 <= nc < n and
                                not visited[nr][nc] and forest[nr][nc] != 0):
                            if nr == end_r and nc == end_c:
                                return steps
                            visited[nr][nc] = True
                            queue.append((nr, nc))

            return -1 

        total_steps = 0
        curr_r, curr_c = 0, 0

        for height, tr, tc in trees:
            dist = bfs(curr_r, curr_c, tr, tc)
            if dist == -1:
                return -1
            total_steps += dist
            curr_r, curr_c = tr, tc

        return total_steps