# 1568. Minimum Number of Days to Disconnect Island

# Hard

# You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.

# The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

# In one day, we are allowed to change any single land cell (1) into a water cell (0).

# Return the minimum number of days to disconnect the grid. 

# Example 1:

# Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]

# Output: 2
# Explanation: We need at least 2 days to get a disconnected grid.
# Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.

# Example 2:

# Input: grid = [[1,1]]
# Output: 2
# Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 30
# grid[i][j] is either 0 or 1.

class Solution:
    def dfs(self, grid: List[List[int]], visited: List[List[bool]], i: int, j: int):
        m, n = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0 or visited[i][j]:
            return
        visited[i][j] = True 
        self.dfs(grid, visited, i+1, j)
        self.dfs(grid, visited, i-1, j)
        self.dfs(grid, visited, i, j+1)
        self.dfs(grid, visited, i, j-1)

    def countIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    count += 1
                    self.dfs(grid, visited, i, j)
        return count
    
    def minDays(self, grid: List[List[int]]) -> int:
        if self.countIslands(grid) != 1:
            return 0
        
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0 
                    if self.countIslands(grid) != 1:
                        return 1
                    grid[i][j] = 1 
        return 2