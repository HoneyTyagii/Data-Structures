# 2257. Count Unguarded Cells in the Grid

# Medium

# You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

# A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

# Return the number of unoccupied cells that are not guarded. 

# Example 1:

# Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
# Output: 7
# Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
# There are a total of 7 unguarded cells, so we return 7.

# Example 2:

# Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
# Output: 4
# Explanation: The unguarded cells are shown in green in the above diagram.
# There are a total of 4 unguarded cells, so we return 4.

# Constraints:

# 1 <= m, n <= 105
# 2 <= m * n <= 105
# 1 <= guards.length, walls.length <= 5 * 104
# 2 <= guards.length + walls.length <= m * n
# guards[i].length == walls[j].length == 2
# 0 <= rowi, rowj < m
# 0 <= coli, colj < n
# All the positions in guards and walls are unique.

class Solution:
    def countUnguarded(self, m: int, n: int, g: list[list[int]], w: list[list[int]]) -> int:
        vis = [[0] * n for _ in range(m)]
        
        for val in w:
            vis[val[0]][val[1]] = 2

        for val in g:
            vis[val[0]][val[1]] = 3

        for val in g:
            row, col = val[0], val[1]

            for i in range(row + 1, m):
                if vis[i][col] in (2, 3):
                    break
                vis[i][col] = 1

            for i in range(row - 1, -1, -1):
                if vis[i][col] in (2, 3):
                    break
                vis[i][col] = 1

            for i in range(col + 1, n):
                if vis[row][i] in (2, 3):
                    break
                vis[row][i] = 1

            for i in range(col - 1, -1, -1):
                if vis[row][i] in (2, 3):
                    break
                vis[row][i] = 1

        unguarded = 0
        for i in range(m):
            for j in range(n):
                if vis[i][j] == 0:
                    unguarded += 1

        return unguarded