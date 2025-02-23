# 889. Construct Binary Tree from Preorder and Postorder Traversal

# Medium

# Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.
# If there exist multiple answers, you can return any of them.

# Example 1:

# Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]

# Example 2:

# Input: preorder = [1], postorder = [1]
# Output: [1] 

# Constraints:

# 1 <= preorder.length <= 30
# 1 <= preorder[i] <= preorder.length
# All the values of preorder are unique.
# postorder.length == preorder.length
# 1 <= postorder[i] <= postorder.length
# All the values of postorder are unique.
# It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.

class Solution:
    def buildTree(self,pre,post,n):
        if n == 0: return
        rootData = pre[0]
        root = TreeNode(rootData)
        if n == 1:
            return root
        data = pre[1]
        rootIdx = -1
        for i in range(n):
            if post[i] == data:
                rootIdx = i
                break
        lefPre = pre[1:rootIdx +2]
        rigPre = pre[rootIdx + 2: ]
        lefPost = post[:rootIdx+1]
        rigPost = post[rootIdx+1:-1]
        root.left = self.buildTree(lefPre,lefPost,len(lefPre))
        root.right = self.buildTree(rigPre,rigPost,len(rigPre))
        return root
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.buildTree(preorder,postorder,len(preorder))