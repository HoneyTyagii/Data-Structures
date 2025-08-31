# 37. Sudoku Solver

# Hard

# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

# Example 1:

# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        Row, Col, Block=[0]*9, [0]*9, [0]*9
        uncertain=[]
        def set3Cond(i, j, x):
            x2=1<<x
            Row[i]|=x2
            Col[j]|=x2
            Block[(i//3)*3 +j//3]|=x2
        def setup():
            for i, row in enumerate(board):
                for j, c in enumerate(row):
                    if c=='.':
                        uncertain.append((i, j))
                    else:
                        set3Cond(i, j, ord(c)-ord('1'))
        def solve(idx):
            if idx==len(uncertain): return True
            i, j=uncertain[idx]
            bidx=(i//3)*3+j//3
            notMask=~(Row[i]|Col[j]|Block[bidx]) & 0b111111111
            while notMask:
                x=notMask.bit_length()-1
                Bit=1<<x
                board[i][j]=chr(ord('1')+x)
                Row[i]|=Bit
                Col[j]|=Bit
                Block[bidx]|=Bit
                if solve(idx+1): return True
                board[i][j]='.'
                Row[i]^=Bit
                Col[j]^=Bit
                Block[bidx]^=Bit
                notMask^=Bit
            return False
        setup()
        solve(0)