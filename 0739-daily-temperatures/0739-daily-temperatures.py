from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  
        
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_idx = stack.pop()
                answer[prev_idx] = i - prev_idx
            stack.append(i)
        
        return answer