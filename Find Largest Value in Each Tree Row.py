# 515. Find Largest Value in Each Tree Row

# Medium

# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

# Example 1:

# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]
# Example 2:

# Input: root = [1,2,3]
# Output: [1,3] 

# Constraints:

# The number of nodes in the tree will be in the range [0, 104].
# -231 <= Node.val <= 231 - 1

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        levelMap = {}
        def dfs(node, level):
            if not node:
                return 
            if level not in levelMap:
                levelMap[level] = node.val
            else:
                if node.val >=  levelMap[level]:
                    levelMap[level] = node.val
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 1)
        res = []
        for i, v in levelMap.items():
            res.append(v)
        return(res)

# Time complexity: O(N)
# Space complexity: O(N)