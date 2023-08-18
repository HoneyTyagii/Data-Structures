# 1615. Maximal Network Rank

# Medium

# There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

# The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

# The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

# Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

 

# Example 1:



# Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
# Output: 4
# Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.
# Example 2:



# Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
# Output: 5
# Explanation: There are 5 roads that are connected to cities 1 or 2.
# Example 3:

# Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
# Output: 5
# Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.
 

# Constraints:

# 2 <= n <= 100
# 0 <= roads.length <= n * (n - 1) / 2
# roads[i].length == 2
# 0 <= ai, bi <= n-1
# ai != bi

class Solution:
	def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
		if roads == []:
			return 0

		node_degrees = defaultdict(int)
		for i in roads:
			node_degrees[i[0]]+=1
			node_degrees[i[1]]+=1

		maxx1, maxx2 = 0, 0
		ans = 0
		for i, k in node_degrees.items():     
			if k >= maxx1:
				maxx1 = k
				maxx2 = 0
				for j, l in node_degrees.items():       
					if l >= maxx2 and j!=i:
						maxx2 = l
						if [i, j] in roads or [j, i] in roads:           
							ans = max(ans, maxx1 + maxx2 - 1)
						else:
							ans = max(ans, maxx1 + maxx2 )
		return ans
	
# time complexity: O(n^2)
# space complexity: O(n)