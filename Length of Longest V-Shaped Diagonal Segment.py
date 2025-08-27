# 3459. Length of Longest V-Shaped Diagonal Segment

# Hard

# You are given a 2D integer matrix grid of size n x m, where each element is either 0, 1, or 2.
# A V-shaped diagonal segment is defined as:
# The segment starts with 1.
# The subsequent elements follow this infinite sequence: 2, 0, 2, 0, ....
# The segment:
# Starts along a diagonal direction (top-left to bottom-right, bottom-right to top-left, top-right to bottom-left, or bottom-left to top-right).
# Continues the sequence in the same diagonal direction.
# Makes at most one clockwise 90-degree turn to another diagonal direction while maintaining the sequence.
# Return the length of the longest V-shaped diagonal segment. If no valid segment exists, return 0.

# Example 1:
# Input: grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
# Output: 5
# Explanation:
# The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,2) → (1,3) → (2,4), takes a 90-degree clockwise turn at (2,4), and continues as (3,3) → (4,2).

# Example 2:
# Input: grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
# Output: 4
# Explanation:
# The longest V-shaped diagonal segment has a length of 4 and follows these coordinates: (2,3) → (3,2), takes a 90-degree clockwise turn at (3,2), and continues as (2,1) → (1,0).

# Example 3:
# Input: grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]
# Output: 5
# Explanation:
# The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,0) → (1,1) → (2,2) → (3,3) → (4,4).

# Example 4:
# Input: grid = [[1]]
# Output: 1
# Explanation:
# The longest V-shaped diagonal segment has a length of 1 and follows these coordinates: (0,0).

# Constraints:

# n == grid.length
# m == grid[i].length
# 1 <= n, m <= 500
# grid[i][j] is either 0, 1 or 2.

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        @cache
        def search(r, c, target, turn, dir):
            if r < 0 or r >= rows or c < 0 or c >= columns or grid[r][c] != target:
                return 0
            
            target = 0 if target == 2 else 2
            total = 0

            if turn:
                if dir == 'top-left': 
                    total = max(total, search(r - 1, c - 1, target, True, 'top-left') + 1)
                elif dir == 'top-right': 
                    total = max(total, search(r - 1, c + 1, target, True, 'top-right') + 1)
                elif dir == 'bottom-left': 
                    total = max(total, search(r + 1, c - 1, target, True, 'bottom-left') + 1)
                elif dir == 'bottom-right': 
                    total = max(total, search(r + 1, c + 1, target, True, 'bottom-right') + 1)
            else:
                if dir == 'top-left': 
                    total = max(total, search(r - 1, c - 1, target, False, 'top-left') + 1)
                    total = max(total, search(r - 1, c + 1, target, True, 'top-right') + 1)
                elif dir == 'top-right': 
                    total = max(total, search(r - 1, c + 1, target, False, 'top-right') + 1)
                    total = max(total, search(r + 1, c + 1, target, True, 'bottom-right') + 1)
                elif dir == 'bottom-left': 
                    total = max(total, search(r + 1, c - 1, target, False, 'bottom-left') + 1)
                    total = max(total, search(r - 1, c - 1, target, True, 'top-left') + 1)
                elif dir == 'bottom-right': 
                    total = max(total, search(r + 1, c + 1, target, False, 'bottom-right') + 1)
                    total = max(total, search(r + 1, c - 1, target, True, 'bottom-left') + 1)
            
            return total
        
        res = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    res = max(res, search(r - 1, c - 1, 2, False, 'top-left') + 1)
                    res = max(res, search(r - 1, c + 1, 2, False, 'top-right') + 1)
                    res = max(res, search(r + 1, c - 1, 2, False, 'bottom-left') + 1)
                    res = max(res, search(r + 1, c + 1, 2, False, 'bottom-right') + 1)
        
        return res