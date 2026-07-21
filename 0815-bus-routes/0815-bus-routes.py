from typing import List
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_to_routes = defaultdict(list)
        for route_idx, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(route_idx)

        visited_routes = set()
        visited_stops = {source}
        queue = deque()

        for route_idx in stop_to_routes[source]:
            if route_idx not in visited_routes:
                visited_routes.add(route_idx)
                queue.append((route_idx, 1))

        while queue:
            route_idx, buses = queue.popleft()

            if target in routes[route_idx]:
                return buses

            for stop in routes[route_idx]:
                if stop not in visited_stops:
                    visited_stops.add(stop)
                    for next_route in stop_to_routes[stop]:
                        if next_route not in visited_routes:
                            visited_routes.add(next_route)
                            queue.append((next_route, buses + 1))

        return -1