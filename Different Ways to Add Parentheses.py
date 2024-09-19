# 241. Different Ways to Add Parentheses

# Medium

# Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

# The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104. 

# Example 1:

# Input: expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0 
# (2-(1-1)) = 2

# Example 2:

# Input: expression = "2*3-4*5"
# Output: [-34,-14,-10,-10,10]
# Explanation:
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10 

# Constraints:

# 1 <= expression.length <= 20
# expression consists of digits and the operator '+', '-', and '*'.
# All the integer values in the input expression are in the range [0, 99].
# The integer values in the input expression do not have a leading '-' or '+' denoting the sign.

class Solution:
    def isOperator(self, ch):
        return ch == '+' or ch == '-' or ch == '*'

    def getDiffWays(self, i, j, expression):
        res = []
        if j - i + 1 <= 2:
            res.append(int(expression[i:j + 1]))
            return res
        for ind in range(i, j + 1):
            if self.isOperator(expression[ind]):
                op = expression[ind]
    
                left = self.getDiffWays(i, ind - 1, expression)
                right = self.getDiffWays(ind + 1, j, expression)
                for l in left:
                    for r in right:
                        if op == '+':
                            res.append(l + r)
                        elif op == '-':
                            res.append(l - r)
                        elif op == '*':
                            res.append(l * r)

        return res

    def diffWaysToCompute(self, expression: str):
        n = len(expression)
        return self.getDiffWays(0, n - 1, expression)