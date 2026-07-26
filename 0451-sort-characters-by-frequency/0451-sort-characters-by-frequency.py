from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        n = len(s)
        
        buckets = [[] for _ in range(n + 1)]
        for char, count in freq.items():
            buckets[count].append(char)
        
        result = []
        for count in range(n, 0, -1):
            for char in buckets[count]:
                result.append(char * count)
        
        return ''.join(result)