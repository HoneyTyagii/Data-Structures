# 498. Diagonal Traverse

# Medium

# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

# Example 1:

# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]

# Example 2:

# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]
 
# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# -105 <= mat[i][j] <= 105

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        f = lambda d: [mat[i][d-i] for i in range(len(mat)) if 0 <= d-i < len(mat[0])]
        return [v for d in range(len(mat)+len(mat[0])-1) for v in f(d)[::(-1)**(d+1)]]