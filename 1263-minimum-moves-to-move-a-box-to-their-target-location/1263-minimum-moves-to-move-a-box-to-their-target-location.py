class Solution:
    def minPushBox(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    player = (i, j)
                elif grid[i][j] == 'B':
                    box = (i, j)
                elif grid[i][j] == 'T':
                    target = (i, j)
        
        def is_wall(r, c):
            return r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '#'
        
        def player_can_reach(start, end, box_pos):
            if start == end:
                return True
            visited = {start}
            queue = deque([start])
            while queue:
                r, c = queue.popleft()
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr, nc = r + dr, c + dc
                    if is_wall(nr, nc) or (nr, nc) == box_pos or (nr, nc) in visited:
                        continue
                    if (nr, nc) == end:
                        return True
                    visited.add((nr, nc))
                    queue.append((nr, nc))
            return False
        
        from collections import deque
        
        start_state = (box[0], box[1], player[0], player[1])
        visited_states = {start_state}
        queue = deque([(start_state, 0)])
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        while queue:
            state, pushes = queue.popleft()
            br, bc, pr, pc = state
            
            if (br, bc) == target:
                return pushes
            
            for dr, dc in directions:
                new_box = (br + dr, bc + dc)
                push_from = (br - dr, bc - dc)
                
                if is_wall(*new_box) or is_wall(*push_from):
                    continue
                
                if player_can_reach((pr, pc), push_from, (br, bc)):
                    new_state = (new_box[0], new_box[1], br, bc)
                    if new_state not in visited_states:
                        visited_states.add(new_state)
                        queue.append((new_state, pushes + 1))
        
        return -1