import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(x*x + y*y, x, y) for x, y in points]
        heapq.heapify(heap)
        
        result = []
        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            result.append([x, y])
        
        return result