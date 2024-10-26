# 2458. Height of Binary Tree After Subtree Removal Queries

# Hard

# You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.

# You have to perform m independent queries on the tree where in the ith query you do the following:

# Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.
# Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.

# Note:

# The queries are independent, so the tree returns to its initial state after each query.
# The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.
 
# Example 1:

# Input: root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]
# Output: [2]
# Explanation: The diagram above shows the tree after removing the subtree rooted at node with value 4.
# The height of the tree is 2 (The path 1 -> 3 -> 2).

# Example 2:

# Input: root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8]
# Output: [3,2,3,2]
# Explanation: We have the following queries:
# - Removing the subtree rooted at node with value 3. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 4).
# - Removing the subtree rooted at node with value 2. The height of the tree becomes 2 (The path 5 -> 8 -> 1).
# - Removing the subtree rooted at node with value 4. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 6).
# - Removing the subtree rooted at node with value 8. The height of the tree becomes 2 (The path 5 -> 9 -> 3).

# Constraints:

# The number of nodes in the tree is n.
# 2 <= n <= 105
# 1 <= Node.val <= n
# All the values in the tree are unique.
# m == queries.length
# 1 <= m <= min(n, 104)
# 1 <= queries[i] <= n
# queries[i] != root.val

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depth_map = defaultdict(lambda :(-1, -1, 0))
        level_map = {}
        def travel(root, level):
            if not root:
                return 0
            depth = max(travel(root.left, level + 1), travel(root.right, level + 1))
            level_map[root.val] = (level, depth)
            max_, second_max, size = depth_map[level]
            if depth >= max_:
                depth_map[level] = (depth, max_, size + 1)
            elif depth > second_max:
                depth_map[level] = (max_, depth, size + 1)
            else:
                depth_map[level] = (max_, second_max, size + 1)
            return depth + 1
        travel(root, 0)
        result = []
        for q in queries:
            level, depth = level_map[q]
            max_, second_max, size = depth_map[level]
            if size == 1:
                result.append(level - 1)
                continue
            if depth == max_:
                result.append(level + second_max)
            else:
                result.append(level + max_) 
        return result