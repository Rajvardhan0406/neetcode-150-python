from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for edge_id, (a, b) in enumerate(connections):
            graph[a].append((b, edge_id))
            graph[b].append((a, edge_id))

        disc = [-1] * n
        low = [0] * n
        bridges = []
        timer = 0

        for start in range(n):
            if disc[start] != -1:
                continue

            stack = [(start, -1, 0)]
            disc[start] = low[start] = timer
            timer += 1

            while stack:
                u, parent_edge_id, i = stack[-1]

                if i < len(graph[u]):
                    v, edge_id = graph[u][i]
                    stack[-1] = (u, parent_edge_id, i + 1)  

                    if edge_id == parent_edge_id:
                        continue
                    if disc[v] == -1:
                        disc[v] = low[v] = timer
                        timer += 1
                        stack.append((v, edge_id, 0))
                    else:
                        low[u] = min(low[u], disc[v])
                else:
                    stack.pop()
                    if stack:
                        parent_u, _, _ = stack[-1]
                        low[parent_u] = min(low[parent_u], low[u])
                        if low[u] > disc[parent_u]:
                            bridges.append([parent_u, u])

        return bridges