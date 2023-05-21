# 934. Shortest Bridge

# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

# An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

# You may change 0's to 1's to connect the two islands to form one island.

# Return the smallest number of 0's you must flip to connect the two islands.

 

# Example 1:

# Input: grid = [[0,1],[1,0]]
# Output: 1
# Example 2:

# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
# Example 3:

# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1
 

# Constraints:

# n == grid.length == grid[i].length
# 2 <= n <= 100
# grid[i][j] is either 0 or 1.
# There are exactly two islands in grid.

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def get_neighbors(i, j):
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= ni < N and 0 <= nj < N:
                    yield ni, nj

        # Find a piece of an island
        start = None
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    start = (i, j)
                    break
            if start:
                break

        # BFS to find perimeter around one island
        q = deque([start])
        seen = set()
        water = set()
        while q:
            i, j = q.popleft()
            if (i, j) in seen:
                continue
            seen.add((i, j))
            for ni, nj in get_neighbors(i, j):
                if grid[ni][nj] == 0:
                    water.add((ni, nj))
                else:
                    q.append((ni, nj))

        # BFS from the perimeter out, until the other island is reached
        q = deque(water)
        res = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if grid[i][j] == 1:
                    return res
                for ni, nj in get_neighbors(i, j):
                    if (ni, nj) in seen:
                        continue
                    seen.add((ni, nj))
                    q.append((ni, nj))
            res += 1