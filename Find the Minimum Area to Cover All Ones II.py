# 3197. Find the Minimum Area to Cover All Ones II

# Hard

# You are given a 2D binary array grid. You need to find 3 non-overlapping rectangles having non-zero areas with horizontal and vertical sides such that all the 1's in grid lie inside these rectangles.
# Return the minimum possible sum of the area of these rectangles.
# Note that the rectangles are allowed to touch.

# Example 1:
# Input: grid = [[1,0,1],[1,1,1]]
# Output: 5
# Explanation:
# The 1's at (0, 0) and (1, 0) are covered by a rectangle of area 2.
# The 1's at (0, 2) and (1, 2) are covered by a rectangle of area 2.
# The 1 at (1, 1) is covered by a rectangle of area 1.

# Example 2:
# Input: grid = [[1,0,1,0],[0,1,0,1]]
# Output: 5
# Explanation:
# The 1's at (0, 0) and (0, 2) are covered by a rectangle of area 3.
# The 1 at (1, 1) is covered by a rectangle of area 1.
# The 1 at (1, 3) is covered by a rectangle of area 1.
 
# Constraints:

# 1 <= grid.length, grid[i].length <= 30
# grid[i][j] is either 0 or 1.
# The input is generated such that there are at least three 1's in grid.

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        @cache
        def minArea(start_row, end_row, start_col, end_col):        
            max_r, max_c = start_row, start_col
            min_r, min_c = end_row, end_col
            
            for row in range(start_row, end_row + 1):
                for col in range(start_col, end_col+1):
                    if grid[row][col] == 1:
                        min_r = min(min_r, row)
                        max_r = max(max_r, row)
                        min_c = min(min_c, col)
                        max_c = max(max_c, col)
            area = (abs(max_c - min_c) + 1) * (abs(max_r - min_r) + 1) 
            return area

        @cache
        def dfs(start_row, end_row, start_col, end_col, remaining):
            if remaining == 1:
                area =  minArea(start_row, end_row, start_col, end_col)
                return area
            
            res = float('inf')
            for v_split in range(start_col, end_col):
                left_full = minArea(start_row, end_row, start_col, v_split)
                right_split = dfs(start_row, end_row, v_split + 1, end_col, remaining - 1) 

                left_split = dfs(start_row, end_row, start_col, v_split, remaining - 1) 
                right_full = minArea(start_row, end_row, v_split + 1, end_col)
                
                res = min(res, left_full + right_split, left_split + right_full)

            for h_split in range(start_row, end_row):
                top_full = minArea(start_row, h_split, start_col, end_col)
                bottom_split = dfs(h_split + 1, end_row, start_col ,end_col, remaining - 1)

                top_split = dfs(start_row, h_split, start_col, end_col, remaining - 1)
                bottom_full = minArea(h_split + 1, end_row, start_col, end_col)

                res = min(res, top_full + bottom_split, top_split + bottom_full)

            return res
        
        return dfs(0, len(grid)-1, 0, len(grid[0])-1, 3)