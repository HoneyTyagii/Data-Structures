# 1895. Largest Magic Square

# Medium

# A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.

# Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found within this grid. 

# Example 1:


# Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
# Output: 3
# Explanation: The largest magic square has a size of 3.
# Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
# - Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
# - Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
# - Diagonal sums: 5+4+3 = 6+4+2 = 12
# Example 2:


# Input: grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
# Output: 2
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j] <= 106

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        maximum = 1

        for i in range(rows):
            for j in range(cols):
                max_side = min(rows - i, cols - j)

                for side in range(maximum + 1, max_side + 1):
                    ref = sum(grid[i][j:j + side])
                    is_magic_sq = True

                    for r in range(i + 1, i + side):
                        if sum(grid[r][j:j + side]) != ref:
                            is_magic_sq = False
                            break

                    if not is_magic_sq:
                        continue

                    for c in range(j, j + side):
                        if sum(grid[r][c] for r in range(i, i + side)) != ref:
                            is_magic_sq = False
                            break

                    if not is_magic_sq:
                        continue

                    if sum(grid[i + s][j + s] for s in range(side)) != ref:
                        continue

                    if sum(grid[i + s][j + side - 1 - s] for s in range(side)) != ref:
                        continue

                    maximum = side

        return maximum