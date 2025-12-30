# 840. Magic Squares In Grid

# Medium

# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

# Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?

# Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15. 

# Example 1:

# Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
# Output: 1
# Explanation: 
# The following subgrid is a 3 x 3 magic square:

# while this one is not:

# In total, there is only one magic square inside the given grid.

# Example 2:

# Input: grid = [[8]]
# Output: 0 

# Constraints:

# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 10
# 0 <= grid[i][j] <= 15

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        magic_square=[
            [4,3,8],
            [9,5,1],
            [2,7,6]
        ]
        def grid_Rotation(grid,k):
            a=grid
            for _ in range(k):
                a=list(zip(*a[::-1]))
            return a
        def number_Of_Rotations(k):
            if k==4: return 0
            if k==2: return 1
            if k==6: return 2
            if k==8: return 3
            return -1
        def is_Identical(grid1,grid2):
            for i in range(3):
                for j in range(3):
                    if grid1[i][j]!=grid2[i][j]:
                        return False
            return True
        def is_transpose(grid1,grid2):
            for i in range(3):
                for j in range(3):
                    if grid1[i][j]!=grid2[j][i]:
                        return False
            return True
        def is_Magic_Square(i,j):
            if grid[i][j]!=5:
                return False
            if i<1 or i>n-2 or j<1 or j>m-2:
                return False
            k=number_Of_Rotations(grid[i-1][j-1])
            if k==-1:
                return False
            rotated=grid_Rotation(magic_square,k)
            return (is_Identical(rotated,[grid[i+x][j-1:j+2] for x in [-1,0,1]])) or (is_transpose(rotated,[grid[i+x][j-1:j+2] for x in [-1,0,1]]))


        if n<=2 or m<=2:
            return 0
        s=0
        for i in range(n):
            for j in range(m):
                if is_Magic_Square(i,j):
                    s+=1
        return s
    
# 2 Approach

class Solution:
    def check(self, i, j, grid):
        magicSum = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
        sum_ = grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]
        vis = [False] * 16
        if sum_ != magicSum:
            return False

        for row in range(i, i+3):
            sum_ = grid[row][j] + grid[row][j+1] + grid[row][j+2]
            vis[grid[row][j]] = True
            vis[grid[row][j+1]] = True
            vis[grid[row][j+2]] = True
            if sum_ != magicSum:
                return False

        for col in range(j, j+3):
            sum_ = grid[i][col] + grid[i+1][col] + grid[i+2][col]
            if sum_ != magicSum:
                return False

        for num in range(1, 10):
            if not vis[num]:
                return False

        return True

    def numMagicSquaresInside(self, grid):
        row = len(grid)
        col = len(grid[0])
        count = 0
        for i in range(row - 2):
            for j in range(col - 2):
                if self.check(i, j, grid):
                    count += 1
        return count