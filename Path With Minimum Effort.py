# 1631. Path With Minimum Effort

# Medium

# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

# Example 1:

# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

# Example 2:

# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

# Example 3:

# Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# Output: 0
# Explanation: This route does not require any effort.

# Constraints:

# rows == heights.length
# columns == heights[i].length
# 1 <= rows, columns <= 100
# 1 <= heights[i][j] <= 106

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        visited  = set()
        h        = []
        drt      = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        
        max_diff = 0
        rows_n   = len(heights)
        cols_n   = len(heights[0])
        
        heappush(h, (max_diff, 0, 0))   
        while True:
            el_dif, el_r, el_c = heappop(h)  
            if (el_r, el_c) in visited:                   
                continue
            visited.add((el_r, el_c))

            max_diff = max(max_diff, el_dif) 
            if (el_r, el_c) == (rows_n - 1, cols_n - 1):   
                break

            for dr_r, dr_c in drt:
                if 0 <= el_r + dr_r < rows_n   and \
                   0 <= el_c + dr_c < cols_n:
                   heappush(h, (abs(heights[el_r][el_c] - heights[el_r + dr_r][el_c + dr_c]), \
el_r + dr_r, el_c + dr_c))
            
        return max_diff
            
            

# time complexity: O(n*m*log(n*m))
# space complexity: O(n*m)