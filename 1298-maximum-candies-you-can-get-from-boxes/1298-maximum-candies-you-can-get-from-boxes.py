from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], 
                    containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        have_box = [False] * n      
        have_key = [False] * n      
        used = [False] * n         
        
        queue = deque()
        total = 0
        
        for b in initialBoxes:
            have_box[b] = True
            if status[b] == 1:
                queue.append(b)
        
        while queue:
            box = queue.popleft()
            if used[box]:
                continue
            used[box] = True
            
            total += candies[box]
            
           
            for k in keys[box]:
                have_key[k] = True
                if have_box[k] and not used[k]:
                    queue.append(k)
            
            
            for cb in containedBoxes[box]:
                have_box[cb] = True
                
                if not used[cb] and (status[cb] == 1 or have_key[cb]):
                    queue.append(cb)
        
        return total