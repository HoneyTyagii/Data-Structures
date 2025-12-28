# 1351. Count Negative Numbers in a Sorted Matrix

# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

# Example 1:

# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:

# Input: grid = [[3,2],[1,0]]
# Output: 0
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum([self.binary_search(arr) for arr in grid])
        
    def binary_search(self, arr):
        start, end = 0, len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] < 0:
                end = mid - 1
            else: 
                start = mid + 1
        return len(arr) - start
    
# 2 Approach

class Solution:
    def countNegatives(self, g: List[List[int]]) -> int:
        return str(g).count('-')