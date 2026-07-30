import random

class RandomizedSet:
    def __init__(self):
        self.arr = []         
        self.idx_map = {}      

    def insert(self, val: int) -> bool:
        if val in self.idx_map:
            return False
        self.idx_map[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx_map:
            return False
        
        idx_to_remove = self.idx_map[val]
        last_val = self.arr[-1]
        
        self.arr[idx_to_remove] = last_val
        self.idx_map[last_val] = idx_to_remove
        
        self.arr.pop()
        del self.idx_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)