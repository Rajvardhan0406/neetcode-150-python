class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        start = "".join(str(x) for row in board for x in row)
        target = "123450"
        
        if start == target:
            return 0
        neighbors_map = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        
        from collections import deque
        visited = {start}
        queue = deque([(start, 0)])
        
        while queue:
            state, moves = queue.popleft()
            zero_idx = state.index("0")
            
            for adj in neighbors_map[zero_idx]:
                new_state = list(state)
                new_state[zero_idx], new_state[adj] = new_state[adj], new_state[zero_idx]
                new_state = "".join(new_state)
                
                if new_state == target:
                    return moves + 1
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves + 1))
        
        return -1