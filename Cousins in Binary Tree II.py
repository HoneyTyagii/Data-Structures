# 2641. Cousins in Binary Tree II

# Medium

# Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.

# Two nodes of a binary tree are cousins if they have the same depth with different parents.

# Return the root of the modified tree.

# Note that the depth of a node is the number of edges in the path from the root node to it. 

# Example 1:

# Input: root = [5,4,9,1,10,null,7]
# Output: [0,0,0,7,7,null,11]
# Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
# - Node with value 5 does not have any cousins so its sum is 0.
# - Node with value 4 does not have any cousins so its sum is 0.
# - Node with value 9 does not have any cousins so its sum is 0.
# - Node with value 1 has a cousin with value 7 so its sum is 7.
# - Node with value 10 has a cousin with value 7 so its sum is 7.
# - Node with value 7 has cousins with values 1 and 10 so its sum is 11.

# Example 2:

# Input: root = [3,1,2]
# Output: [0,0,0]
# Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
# - Node with value 3 does not have any cousins so its sum is 0.
# - Node with value 1 does not have any cousins so its sum is 0.
# - Node with value 2 does not have any cousins so its sum is 0.
 
# Constraints:

# The number of nodes in the tree is in the range [1, 105].
# 1 <= Node.val <= 104


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def level_sum(root):
            if not root:
                return []

            result = []
            queue = [root]

            while queue:
                current_level_sum = 0
                level_size = len(queue)

                for _ in range(level_size):
                    node = queue.pop(0)
                    current_level_sum += node.val

                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)

                result.append(current_level_sum)

            return result

        levels_sum = level_sum(root)
        print(levels_sum)

        def copy_tree(node):
            if node is None:
                return None
            new_node = TreeNode(node.val)
            new_node.left = copy_tree(node.left)
            new_node.right = copy_tree(node.right)
            return new_node

        ans_tree = copy_tree(root)

        def dfs(node, parent, level, ans):
            if node is None:
                return
            level_sum = levels_sum[level]
            if level < 2:
                ans.val = 0
            else:
                left_val = 0 if not parent.left else parent.left.val
                right_val = 0 if not parent.right else parent.right.val
                new_val = level_sum - left_val - right_val
                ans.val = new_val
            dfs(node.left, node, level+1, ans.left)
            dfs(node.right, node, level+1, ans.right)

        dfs(root, None, 0, ans_tree)
        return ans_tree