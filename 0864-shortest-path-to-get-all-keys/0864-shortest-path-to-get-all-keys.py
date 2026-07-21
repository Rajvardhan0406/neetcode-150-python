from typing import List
from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])

        start_row = start_col = 0
        num_keys = 0

        for r in range(m):
            for c in range(n):
                cell = grid[r][c]
                if cell == '@':
                    start_row, start_col = r, c
                elif cell.islower():
                    num_keys += 1

        target_mask = (1 << num_keys) - 1
        visited = set()
        start_state = (start_row, start_col, 0)
        visited.add(start_state)
        queue = deque([(start_row, start_col, 0, 0)]) 
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            row, col, mask, dist = queue.popleft()

            if mask == target_mask:
                return dist

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n:
                    cell = grid[nr][nc]
                    if cell == '#':
                        continue

                    new_mask = mask
                    if cell.isupper():
                       
                        key_bit = 1 << (ord(cell.lower()) - ord('a'))
                        if not (mask & key_bit):
                            continue 
                    elif cell.islower():
                        new_mask = mask | (1 << (ord(cell) - ord('a')))

                    new_state = (nr, nc, new_mask)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((nr, nc, new_mask, dist + 1))

        return -1