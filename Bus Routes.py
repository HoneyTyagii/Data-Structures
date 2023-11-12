# 815. Bus Routes

# Hard

# You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

# For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
# You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

# Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

# Example 1:

# Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# Output: 2
# Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
# Example 2:

# Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
# Output: -1
 

# Constraints:

# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 105
# All the values of routes[i] are unique.
# sum(routes[i].length) <= 105
# 0 <= routes[i][j] < 106
# 0 <= source, target < 106

class Solution:
      def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        graph = defaultdict(set)  
        for route_id, stops in enumerate(routes):
            for stop in stops:
                graph[stop].add(route_id)  
        
        queue = deque([(source, 0)])
        seen_stops = set([source])
        seen_routes = set()
        
        while queue:
            stop, num_changes = queue.popleft()
            if stop == target:
                return num_changes
            for route_id in graph[stop]:
                if route_id not in seen_routes:
                    seen_routes.add(route_id)
                    for stop in routes[route_id]:
                        if stop not in seen_stops:
                            seen_stops.add(stop)
                            queue.append((stop, num_changes + 1))
        
        return -1

# time complexity : O(m∗n)
# space complexity : O(m∗n)