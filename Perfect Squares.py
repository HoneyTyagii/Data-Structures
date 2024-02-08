# 279. Perfect Squares

# Medium

# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not. 

# Example 1:

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
 

# Constraints:

# 1 <= n <= 104

class Solution:
    def numSquares(self, n: int) -> int:

        def CheckTwo(c):                       
            while c%2==0: c//= 2
            while c%5==0: c//= 5
            while c%9==0: c//= 9

            if c%3==0: return False

            if c in (0,1,13,17): return True

            i, j = 0, isqrt(c)

            while i <= j:
                if i*i + j*j == c: return True
                if i*i + j*j < c: i += 1
                if i*i + j*j > c: j -= 1

            return  False


        if n == isqrt(n)**2:return 1                

        if CheckTwo(n): return 2                    

        while n%4 ==0: n//=4                        
        if n%8 != 7: return 3 
        
        return 4                                    