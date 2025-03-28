# 2503. Maximum Number of Points From Grid Queries

# Hard

# You are given an m x n integer matrix grid and an array queries of size k.
# Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:
# If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
# Otherwise, you do not get any points, and you end this process.
# After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.
# Return the resulting array answer.

# Example 1:

# Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
# Output: [5,8,1]
# Explanation: The diagrams above show which cells we visit to get points for each query.

# Example 2:

# Input: grid = [[5,2,1],[1,1,2]], queries = [3]
# Output: [0]
# Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3. 

# Constraints:

# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 1000
# 4 <= m * n <= 105
# k == queries.length
# 1 <= k <= 104
# 1 <= grid[i][j], queries[i] <= 106

import heapq
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        k = len(queries)

        query_ind = sorted(range(k), key=lambda i: queries[i])
        res = [0] * k

        min_heap = [(grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True

        cnt = 0 
        for i in query_ind:
            q = queries[i]
            while min_heap and min_heap[0][0] < q:
                val, r, c = heapq.heappop(min_heap)
                cnt += 1

                for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<m and 0<=nc<n and not visited[nr][nc]:
                        heapq.heappush(min_heap, (grid[nr][nc], nr, nc))
                        visited[nr][nc] = True

            res[i] = cnt 
        return res