import heapq
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)
        
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)
        
        route = []
        
        def dfs(airport: str) -> None:
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])
                dfs(next_airport)
            route.append(airport)
        
        dfs("JFK")
        
        return route[::-1]