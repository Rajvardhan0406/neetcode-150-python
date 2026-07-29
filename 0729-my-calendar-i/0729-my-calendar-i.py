from sortedcontainers import SortedList

class MyCalendar:
    def __init__(self):
        self.bookings = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        idx = self.bookings.bisect_left((startTime, endTime))
        
        if idx < len(self.bookings) and self.bookings[idx][0] < endTime:
            return False
        
        if idx > 0 and self.bookings[idx - 1][1] > startTime:
            return False
        
        self.bookings.add((startTime, endTime))
        return True