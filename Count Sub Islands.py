# 1905. Count Sub Islands

# Medium

# You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

# An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

# Return the number of islands in grid2 that are considered sub-islands. 

# Example 1:

# Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# Output: 3
# Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.

# Example 2:

# Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
# Output: 2 
# Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands. 

# Constraints:

# m == grid1.length == grid2.length
# n == grid1[i].length == grid2[i].length
# 1 <= m, n <= 500
# grid1[i][j] and grid2[i][j] are either 0 or 1.

class Solution:
    def check_islands(self, grid1, grid2, row, col):
        if row < 0 or row >= len(grid2) or col < 0 or col >= len(grid2[0]) or grid2[row][col] == 0: 
            return True
        elif (grid1[row][col] == 0 and grid2[row][col] == 1) or (grid1[row][col] == 1 and grid2[row][col] == 0):
            return False
        elif grid1[row][col] == 1 and grid2[row][col] == 1:
            grid2[row][col] = 0            
        
            left = self.check_islands(grid1, grid2, row, col - 1)
            right = self.check_islands(grid1, grid2, row, col + 1)
            top = self.check_islands(grid1, grid2, row - 1, col)
            bottom = self.check_islands(grid1, grid2, row + 1, col)
            return left and right and top and bottom
    
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        num_sub_islands = 0 
        for row in range(len(grid2)):
            for col in range(len(grid2[row])):
                if grid2[row][col] == 1 and self.check_islands(grid1, grid2, row, col): 
                    num_sub_islands += 1
        return num_sub_islands