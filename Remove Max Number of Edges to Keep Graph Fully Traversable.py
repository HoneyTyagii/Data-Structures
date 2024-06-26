# 1579. Remove Max Number of Edges to Keep Graph Fully Traversable

# Alice and Bob have an undirected graph of n nodes and three types of edges:

# Type 1: Can be traversed by Alice only.
# Type 2: Can be traversed by Bob only.
# Type 3: Can be traversed by both Alice and Bob.
# Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

# Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

 

# Example 1:



# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
# Output: 2
# Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
# Example 2:



# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
# Output: 0
# Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
# Example 3:



# Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
# Output: -1
# Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.
 

 

# Constraints:

# 1 <= n <= 105
# 1 <= edges.length <= min(105, 3 * n * (n - 1) / 2)
# edges[i].length == 3
# 1 <= typei <= 3
# 1 <= ui < vi <= n
# All tuples (typei, ui, vi) are distinct.



class Solution:
    def maxNumEdgesToRemove(self, n, edges):
        
        def find(i, root):
            if i != root[i]:
                root[i] = find(root[i], root)
            return root[i]

        def uni(x, y, root):
            x, y = find(x, root), find(y, root)
            if x == y: return 0
            root[x] = y
            return 1

        res = alice_edges = bob_edges = 0

        
        root = list(range(n + 1))
        for t, i, j in edges:
            if t == 3:
                if uni(i, j, root):
                    alice_edges += 1
                    bob_edges += 1
                else:
                    res += 1
        root0 = root[:]

        
        for t, i, j in edges:
            if t == 1:
                if uni(i, j, root):
                    alice_edges += 1
                else:
                    res += 1

        
        root = root0
        for t, i, j in edges:
            if t == 2:
                if uni(i, j, root):
                    bob_edges += 1
                else:
                    res += 1

        return res if alice_edges == bob_edges == n - 1 else -1
    
# 2 Approach
    
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice_nodes = [-1] * (n + 1)
        bob_nodes = [-1] * (n + 1)

        def helper_find_parent(family, node):
            if family[node] < 0:
                return node
            family[node] = helper_find_parent(family, family[node])
            return family[node]

        num_redundant_edges = 0

        for typ, u, v in edges:
            if typ == 3:
                p_u = helper_find_parent(alice_nodes, u)
                p_v = helper_find_parent(alice_nodes, v)

                if p_u != p_v:
                    alice_nodes[p_u] += alice_nodes[p_v]
                    alice_nodes[p_v] = p_u
                else:
                    num_redundant_edges += 1
        bob_nodes = alice_nodes.copy()
        for typ, u, v in edges:
            if typ == 1:
                p_u = helper_find_parent(alice_nodes, u)
                p_v = helper_find_parent(alice_nodes, v)

                if p_u != p_v:
                    alice_nodes[p_u] += alice_nodes[p_v]
                    alice_nodes[p_v] = p_u
                else:
                    num_redundant_edges += 1

            if typ == 2:
                p_u = helper_find_parent(bob_nodes, u)
                p_v = helper_find_parent(bob_nodes, v)

                if p_u != p_v:
                    bob_nodes[p_u] += bob_nodes[p_v]
                    bob_nodes[p_v] = p_u
                else:
                    num_redundant_edges += 1
        al = min(alice_nodes)
        bl = min(bob_nodes)
        if (al == bl and al == -1 * n):
            return num_redundant_edges
        else:
            return -1
