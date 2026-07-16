import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Step 1: Build adjacency list
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Step 2: Dijkstra's algorithm using min-heap
        dist = {}  # node -> shortest distance from k
        min_heap = [(0, k)]  
        
        while min_heap:
            d, node = heapq.heappop(min_heap)
            
            if node in dist: 
                continue
            dist[node] = d
            
            for neighbor, weight in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(min_heap, (d + weight, neighbor))
        
       
        if len(dist) != n:
            return -1
        
        return max(dist.values())