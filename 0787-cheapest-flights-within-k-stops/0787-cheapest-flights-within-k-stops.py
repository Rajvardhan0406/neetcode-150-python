class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0
        
        for _ in range(k + 1):
            temp = dist.copy()
            for u, v, price in flights:
                if dist[u] != INF and dist[u] + price < temp[v]:
                    temp[v] = dist[u] + price
            dist = temp
        
        return dist[dst] if dist[dst] != INF else -1