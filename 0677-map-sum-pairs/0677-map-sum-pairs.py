class TrieNode:
    def __init__(self):
        self.children = {}
        self.val_sum = 0

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.key_map = {}  

    def insert(self, key: str, val: int) -> None:
        delta = val - self.key_map.get(key, 0)
        self.key_map[key] = val

        node = self.root
        node.val_sum += delta
        for ch in key:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.val_sum += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.val_sum