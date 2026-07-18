from collections import deque, defaultdict
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        L = len(beginWord)
        
        pattern_map = defaultdict(list)
        for word in word_set:
            for i in range(L):
                pattern = word[:i] + '*' + word[i+1:]
                pattern_map[pattern].append(word)
        
        # BFS
        visited = {beginWord}
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, length = queue.popleft()
            
            if word == endWord:
                return length
            
            for i in range(L):
                pattern = word[:i] + '*' + word[i+1:]
                for neighbor in pattern_map[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, length + 1))
                pattern_map[pattern] = []
        
        return 0