from typing import List
from bisect import bisect_right

class TimeMap:

    def __init__(self):
       
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        arr = self.store[key]
        lo, hi = 0, len(arr) - 1
        result = ""
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid][0] <= timestamp:
                result = arr[mid][1]   
                lo = mid + 1
            else:
                hi = mid - 1
        
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestam