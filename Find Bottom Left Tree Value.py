# 513. Find Bottom Left Tree Value

# Medium

# Given the root of a binary tree, return the leftmost value in the last row of the tree. 

# Example 1:

# Input: root = [2,1,3]
# Output: 1
# Example 2:

# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        l=defaultdict(list)
        def bfs(root,h):
            if root is None:
                return
            l[h].append(root.val)
            bfs(root.left,h+1)
            bfs(root.right,h+1)
        bfs(root,0)
        return l[len(l)-1][0]