import heapq
from collections import defaultdict
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float],
                        start: int, end: int) -> float:
        graph = defaultdict(list)
        for (a, b), prob in zip(edges, succProb):
            graph[a].append((b, prob))
            graph[b].append((a, prob))

        max_prob = [0.0] * n
        max_prob[start] = 1.0

        heap = [(-1.0, start)]

        while heap:
            neg_prob, node = heapq.heappop(heap)
            prob = -neg_prob

            if node == end:
                return prob

            if prob < max_prob[node]:
                continue

            for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(heap, (-new_prob, neighbor))

        return 0.0