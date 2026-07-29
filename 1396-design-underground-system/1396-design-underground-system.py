class UndergroundSystem:
    def __init__(self):
        self.checkins = {}  
        self.trips = {}     

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkins.pop(id)
        key = (startStation, stationName)
        travel_time = t - startTime
        
        if key not in self.trips:
            self.trips[key] = [0, 0]
        self.trips[key][0] += travel_time
        self.trips[key][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.trips[(startStation, endStation)]
        return total_time / count