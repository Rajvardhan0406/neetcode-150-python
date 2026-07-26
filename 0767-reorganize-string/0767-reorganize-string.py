import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        count = Counter(s)
        
        max_freq = max(count.values())
        if max_freq > (n + 1) // 2:
            return ""
        
        heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(heap)
        
        result = []
        prev_freq, prev_char = 0, ''
        
        while heap:
            freq, char = heapq.heappop(heap)
            result.append(char)
            
            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_char))
            
            prev_freq, prev_char = freq + 1, char
        
        return ''.join(result)