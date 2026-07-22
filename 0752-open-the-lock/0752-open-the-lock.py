class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        dead = set(deadends)
        start = "0000"
        
        if start in dead:
            return -1
        if target == start:
            return 0
        
        from collections import deque
        visited = {start}
        queue = deque([(start, 0)])
        
        while queue:
            state, moves = queue.popleft()
            
            for i in range(4):
                digit = int(state[i])
                for delta in (-1, 1):
                    new_digit = (digit + delta) % 10
                    new_state = state[:i] + str(new_digit) + state[i+1:]
                    
                    if new_state in dead or new_state in visited:
                        continue
                    if new_state == target:
                        return moves + 1
                    
                    visited.add(new_state)
                    queue.append((new_state, moves + 1))
        
        return -1