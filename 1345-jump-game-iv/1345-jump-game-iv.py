from collections import defaultdict, deque
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        value_to_indices = defaultdict(list)
        for i, v in enumerate(arr):
            value_to_indices[v].append(i)
        visited = [False] * n
        visited[0] = True
        queue = deque([0])
        steps = 0
        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()

                if i == n - 1:
                    return steps

               
                if arr[i] in value_to_indices:
                    for j in value_to_indices[arr[i]]:
                        if not visited[j]:
                            visited[j] = True
                            queue.append(j)
                  
                    del value_to_indices[arr[i]]
                if i + 1 < n and not visited[i + 1]:
                    visited[i + 1] = True
                    queue.append(i + 1)

               
                if i - 1 >= 0 and not visited[i - 1]:
                    visited[i - 1] = True
                    queue.append(i - 1)

            steps += 1

        return -1  