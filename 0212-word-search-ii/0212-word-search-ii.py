from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None 


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, parent):
            ch = board[r][c]
            node = parent.children.get(ch)
            if node is None:
                return

            if node.word is not None:
                result.append(node.word)
                node.word = None  

            board[r][c] = '#'  
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, node)
            board[r][c] = ch  

            
            if not node.children:
                parent.children.pop(ch, None)

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result