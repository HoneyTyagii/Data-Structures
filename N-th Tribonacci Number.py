# 1137. N-th Tribonacci Number

# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
            
# Given n, return the value of Tn.                  
         
                    

# Example 1:

# Input: n = 4
# Output: 4            
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
# Example 2:

# Input: n = 25
# Output: 1389537
 
           
# Constraints:                
                   
# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.            

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            a, b, c = 0, 1, 1
            for i in range(3, n + 1):
                a, b, c = b, c, a + b + c
            return c                           
        

# 2 Approach
        
class Tri:
    n = 38
    nums = [0] * n

    def tribo(self, k):
        if k == 0:
            return 0
        if self.nums[k] != 0:
            return self.nums[k]

        self.nums[k] = self.tribo(k - 1) + self.tribo(k - 2) + self.tribo(k - 3)
        return self.nums[k]

    def __init__(self):
        self.nums[1] = 1
        self.nums[2] = 1
        self.tribo(self.n - 1)

class Solution:
    t = Tri()

    def tribonacci(self, n):
        return Solution.t.nums[n]