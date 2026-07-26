import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        
        class Node:
            __slots__ = ('freq', 'word')
            def __init__(self, freq, word):
                self.freq = freq
                self.word = word
           
            def __lt__(self, other):
                if self.freq != other.freq:
                    return self.freq < other.freq
                return self.word > other.word
        
        heap = []
        for word, freq in count.items():
            heapq.heappush(heap, Node(freq, word))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = [heapq.heappop(heap).word for _ in range(k)]
        result.reverse()
        return result