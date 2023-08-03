# Distance from the Source (Bellman-Ford Algorithm)

# Medium

# Given a weighted, directed and connected graph of V vertices and E edges, Find the shortest distance of all the vertex's from the source vertex S.
# Note: If the Graph contains a negative cycle then return an array consisting of only -1.

# Example 1:

# Input:

# E = [[0,1,9]]
# S = 0
# Output:
# 0 9
# Explanation:
# Shortest distance of all nodes from
# source is printed.
# Example 2:

# Input:

# E = [[0,1,5],[1,0,3],[1,2,-1],[2,0,1]]
# S = 2
# Output:
# 1 6 0
# Explanation:
# For nodes 2 to 0, we can follow the path-
# 2-0. This has a distance of 1.
# For nodes 2 to 1, we cam follow the path-
# 2-0-1, which has a distance of 1+5 = 6,
 

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function bellman_ford( ) which takes a number of vertices V and an E-sized list of lists of three integers where the three integers are u,v, and w; denoting there's an edge from u to v, which has a weight of w and source node S as input parameters and returns a list of integers where the ith integer denotes the distance of an ith node from the source node.

# If some node isn't possible to visit, then its distance should be 100000000(1e8). Also, If the Graph contains a negative cycle then return an array consisting of only -1.
 

# Constraints:
# 1 ≤ V ≤ 500
# 1 ≤ E ≤ V*(V-1)
# -1000 ≤ adj[i][j] ≤ 1000
# 0 ≤ S < V

class Solution:
    def bellman_ford(self, V, edges, S):
        
        dist = [float('inf') for i in range(V)]
        dist[S] = 0
        for i in range(V-1):
            for u, v, w in edges:
                if dist[u] != float('inf') and dist[v]>w+dist[u] :
                    dist[v] = min(dist[v], dist[u] + w)
                    
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                return [-1]
                
        for i in range(len(dist)):
            if dist[i] == float('inf'):
                dist[i] = 100000000
        return dist


# time complexity: O(VE)
# space complexity: O(V)