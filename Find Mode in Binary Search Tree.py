# 501. Find Mode in Binary Search Tree

# Easy

# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

# If the tree has more than one mode, return them in any order.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees. 

# Example 1:

# Input: root = [1,null,2,2]
# Output: [2]
# Example 2:

# Input: root = [0]
# Output: [0]

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:

        self.mode_count = 0
        self.current_val = None
        self.current_count = 0
        self.mode_list = []
        
        def update_mode_list(val):
            if self.current_count > self.mode_count:
                self.mode_count = self.current_count
                self.mode_list = [val]
            elif self.current_count == self.mode_count:
                self.mode_list.append(val)
        
        def traverse(node):
            if node is None:
                return
            
            traverse(node.left)
            
            if node.val == self.current_val:
                self.current_count += 1
            else:
                update_mode_list(self.current_val)
                self.current_val = node.val
                self.current_count = 1
            
            traverse(node.right)
        
        traverse(root)
        
        update_mode_list(self.current_val)
        
        return self.mode_list

# time complexity: O(n)
# space complexity: O(n)  