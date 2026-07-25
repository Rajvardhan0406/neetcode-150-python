class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1001
        for num, start, end in trips:
            diff[start] += num
            diff[end] -= num
        
        passengers = 0
        for change in diff:
            passengers += change
            if passengers > capacity:
                return False
        return True