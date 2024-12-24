# 3203. Find Minimum Diameter After Merging Two Trees

# Hard

# There exist two undirected trees with n and m nodes, numbered from 0 to n - 1 and from 0 to m - 1, respectively. You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.

# You must connect one node from the first tree with another node from the second tree with an edge.

# Return the minimum possible diameter of the resulting tree.

# The diameter of a tree is the length of the longest path between any two nodes in the tree. 

# Example 1:

# Input: edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]

# Output: 3

# Explanation:

# We can obtain a tree of diameter 3 by connecting node 0 from the first tree with any node from the second tree.

# Example 2:

# Input: edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]

# Output: 5

# Explanation:

# We can obtain a tree of diameter 5 by connecting node 0 from the first tree with node 0 from the second tree.

# Constraints:

# 1 <= n, m <= 105
# edges1.length == n - 1
# edges2.length == m - 1
# edges1[i].length == edges2[i].length == 2
# edges1[i] = [ai, bi]
# 0 <= ai, bi < n
# edges2[i] = [ui, vi]
# 0 <= ui, vi < m
# The input is generated such that edges1 and edges2 represent valid trees.

from collections import defaultdict

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def build_graph(edges):
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph

        def find_tree_info(edges):
            graph = build_graph(edges)
            
            def dfs(node, parent):
                height, diameter = 0, 0
                max_height1, max_height2 = 0, 0
                for child in graph[node]:
                    if child != parent:
                        child_height, child_diameter = dfs(child, node)
                        diameter = max(diameter, child_diameter)
                        if child_height + 1 > max_height1:
                            max_height2 = max_height1
                            max_height1 = child_height + 1
                        elif child_height + 1 > max_height2:
                            max_height2 = child_height + 1
                
                diameter = max(diameter, max_height1 + max_height2)
                return max_height1, diameter

            _, diameter = dfs(0, -1)
            return diameter, min(len(graph) - 1, (diameter + 1) // 2)

        diameter1, height1 = find_tree_info(edges1)
        diameter2, height2 = find_tree_info(edges2)

        return max(diameter1, diameter2, height1 + height2 + 1)