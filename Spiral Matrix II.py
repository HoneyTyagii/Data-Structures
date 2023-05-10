# 59. Spiral Matrix II

# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

# Example 1:


# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# Example 2:

# Input: n = 1
# Output: [[1]]
 

# Constraints:

# 1 <= n <= 20

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_dir = 0
        x, y = 0, 0
        for num in range(1, n * n + 1):
            matrix[x][y] = num
            next_x, next_y = x + direction[curr_dir][0], y + direction[curr_dir][1]
            if 0 <= next_x < n and 0 <= next_y < n and matrix[next_x][next_y] == 0:
                x, y = next_x, next_y
            else:
                curr_dir = (curr_dir + 1) % 4
                x, y = x + direction[curr_dir][0], y + direction[curr_dir][1]
        return matrix