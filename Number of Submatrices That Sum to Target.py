# 1074. Number of Submatrices That Sum to Target

# Hard

# Given a matrix and a target, return the number of non-empty submatrices that sum to target.

# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'. 

# Example 1:

# Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# Output: 4
# Explanation: The four 1x1 submatrices that only contain 0.
# Example 2:

# Input: matrix = [[1,-1],[-1,1]], target = 0
# Output: 5
# Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
# Example 3:

# Input: matrix = [[904]], target = 0
# Output: 0
 
# Constraints:

# 1 <= matrix.length <= 100
# 1 <= matrix[0].length <= 100
# -1000 <= matrix[i] <= 1000
# -10^8 <= target <= 10^8

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        h, w = len(matrix), len(matrix[0])
        for y in range(h):
            for x in range(1,w):
                matrix[y][x] = matrix[y][x] + matrix[y][x-1]
        counter = 0
        for left in range(w):
            for right in range(left, w):
                accumulation = {0: 1}
                area = 0
                for y in range(h):
                    if left > 0:
                        area += matrix[y][right] - matrix[y][left-1]
                    else:
                        area += matrix[y][right]
                    counter += accumulation.get( area - target, 0)
                    accumulation[area] = accumulation.get(area, 0) + 1
        return counter