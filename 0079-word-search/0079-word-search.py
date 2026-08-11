class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        n = len(word)

        def backtrack(r: int, c: int, idx: int) -> bool:
            if idx == n:
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if board[r][c] != word[idx]:
                return False

            temp = board[r][c]
            board[r][c] = '#'

            found = (backtrack(r + 1, c, idx + 1) or
                     backtrack(r - 1, c, idx + 1) or
                     backtrack(r, c + 1, idx + 1) or
                     backtrack(r, c - 1, idx + 1))

            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False