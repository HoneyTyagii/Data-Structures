# 2385. Amount of Time for Binary Tree to Be Infected

# Medium

# You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

# Each minute, a node becomes infected if:

# The node is currently uninfected.
# The node is adjacent to an infected node.
# Return the number of minutes needed for the entire tree to be infected. 

# Example 1:

# Input: root = [1,5,3,null,4,10,6,9,2], start = 3
# Output: 4
# Explanation: The following nodes are infected during:
# - Minute 0: Node 3
# - Minute 1: Nodes 1, 10 and 6
# - Minute 2: Node 5
# - Minute 3: Node 4
# - Minute 4: Nodes 9 and 2
# It takes 4 minutes for the whole tree to be infected so we return 4.
# Example 2:


# Input: root = [1], start = 1
# Output: 0
# Explanation: At minute 0, the only node in the tree is infected so we return 0.
 
# Constraints:

# The number of nodes in the tree is in the range [1, 105].
# 1 <= Node.val <= 105
# Each node has a unique value.
# A node with a value of start exists in the tree.

class Solution:
    def amountOfTime(self, root, start: int) -> int:
        time_to_infect_tree, _ = self.dfs(root, start)
        return time_to_infect_tree

    def dfs(self, root, start):
        if root == None:
            return -1, -1

        left_infect_time, left_distance = self.dfs(root.left, start)
        right_infect_time, right_distance = self.dfs(root.right, start)
		
        if left_distance == -1 and right_distance == -1:
            distance = -1
            infect_time = max(right_infect_time, left_infect_time) + 1

        elif left_distance != -1:
            distance = left_distance + 1
            infect_time = max(left_infect_time, right_infect_time + left_distance + 2)
           
        else:
            distance = right_distance + 1
            infect_time = max(right_infect_time, left_infect_time + right_distance + 2)

        if root.val == start:
            distance = 0 

        return infect_time, distance