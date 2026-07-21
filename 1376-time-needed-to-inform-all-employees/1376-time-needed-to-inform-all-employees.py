from typing import List
from collections import deque

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = [[] for _ in range(n)]
        for employee, mgr in enumerate(manager):
            if mgr != -1:
                children[mgr].append(employee)

        max_time = 0
        queue = deque([(headID, 0)])  

        while queue:
            emp, time_so_far = queue.popleft()
            max_time = max(max_time, time_so_far)
            for child in children[emp]:
                queue.append((child, time_so_far + informTime[emp]))

        return max_time