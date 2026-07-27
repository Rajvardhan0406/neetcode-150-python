from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())
        max_count = sum(1 for f in freq.values() if f == max_freq)
        
        frame_length = (max_freq - 1) * (n + 1) + max_count
        
        return max(frame_length, len(tasks))