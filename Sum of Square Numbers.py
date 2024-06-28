# 633. Sum of Square Numbers

# Medium

# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c. 

# Example 1:

# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5

# Example 2:

# Input: c = 3
# Output: false

# Constraints:

# 0 <= c <= 231 - 1

from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(sqrt(c)) + 1):  
            b = sqrt(c - a * a) 
            if b == int(b): 
                return True  
        return False  