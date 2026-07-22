class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)

        def get_pos(square):
            r, c = divmod(square - 1, n)
            row = n - 1 - r
            col = c if r % 2 == 0 else n - 1 - c
            return row, col

        target = n * n
        visited = [False] * (target + 1)
        visited[1] = True
        from collections import deque
        queue = deque([(1, 0)])  

        while queue:
            curr, moves = queue.popleft()
            if curr == target:
                return moves
            for nxt in range(curr + 1, min(curr + 6, target) + 1):
                r, c = get_pos(nxt)
                dest = board[r][c] if board[r][c] != -1 else nxt
                if not visited[dest]:
                    visited[dest] = True
                    queue.append((dest, moves + 1))

        return -1