# 1339. Maximum Product of Splitted Binary Tree

# Medium

# Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

# Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

# Note that you need to maximize the answer before taking the mod and not after taking it.

# Example 1:

# Input: root = [1,2,3,4,5,6]
# Output: 110
# Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
# Example 2:


# Input: root = [1,null,2,3,4,null,null,5,6]
# Output: 90
# Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
 

# Constraints:

# The number of nodes in the tree is in the range [2, 5 * 104].
# 1 <= Node.val <= 104

class Solution:
    def __init__(self):
        self.totalSum = 0
        self.max = 0

    def dfs(self, root):
        if root is None:
            return 0
        return root.val + self.dfs(root.left) + self.dfs(root.right)

    def postOrder(self, root):
        if root is None:
            return 0
        sum = root.val + self.postOrder(root.left) + self.postOrder(root.right)
        self.max = self.max if self.max > (self.totalSum - sum) * sum else (self.totalSum - sum) * sum
        return sum

    def maxProduct(self, root):
        self.totalSum = self.dfs(root)
        self.max = 0
        self.postOrder(root)
        return int(self.max % 1000000007)