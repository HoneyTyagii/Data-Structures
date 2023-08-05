# 95. Unique Binary Search Trees II

# Medium

# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

# Example 1:

# Input: n = 3
# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
# Example 2:

# Input: n = 1
# Output: [[1]]

# Constraints:

# 1 <= n <= 8

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
   def generateTrees(self, n: 'int') -> 'List[TreeNode]':
    memo = {}
    
    def generate_trees_helper(start: int, end: int) -> List[TreeNode]:
        if start > end:
            return [None]
        
        if (start, end) in memo:
            return memo[(start, end)]
        
        result = []
        
        for i in range(start, end+1):
            left_subtrees = generate_trees_helper(start, i-1)
            right_subtrees = generate_trees_helper(i+1, end)
            
            for left in left_subtrees:
                for right in right_subtrees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    result.append(root)
        
        memo[(start, end)] = result
        
        return result
    
    return generate_trees_helper(1, n)
   
# time complexity: O(n^2)
# space complexity: O(n^2)