# 1277. Count Square Submatrices with All Ones

# Medium

# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones. 

# Example 1:

# Input: matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# Output: 15
# Explanation: 
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.

# Example 2:

# Input: matrix = 
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# Output: 7
# Explanation: 
# There are 6 squares of side 1.  
# There is 1 square of side 2. 
# Total number of squares = 6 + 1 = 7. 

# Constraints:

# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1

class Solution(object):
    def countSquares(self, matrix):
        m, n = len(matrix), len(matrix[0])

        @cache
        def dp(i,j):
            if matrix[i][j]==1 : 
                if i!=0 and j!=0:
                    return min(dp(i-1,j), dp(i,j-1), dp(i-1,j-1))+1
                else:
                    return 0+1
            else:
                return 0
        
        return sum(dp(i,j) for i in range(m) for j in range(n))


# 2 Approach
    
class Solution:
    def countSquares(self, g: List[List[int]]) -> int:
        return sum(starmap(f:=cache(lambda i,j:i*j*g[i][j] and 1+min(f(i,j-1),f(i-1,j-1),f(i-1,j)) or g[i][j]),product(range(len(g)),range(len(g[0])))))