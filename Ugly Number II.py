# 264. Ugly Number II

# Medium

# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return the nth ugly number. 

# Example 1:

# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

# Example 2:

# Input: n = 1
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5. 

# Constraints:

# 1 <= n <= 1690

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        k = [0] * n
        t1 = t2 = t3 = 0
        k[0] = 1
        for i in range(1,n):
            k[i] = min(k[t1]*2,k[t2]*3,k[t3]*5)
            if(k[i] == k[t1]*2): t1 += 1
            if(k[i] == k[t2]*3): t2 += 1
            if(k[i] == k[t3]*5): t3 += 1
        return k[n-1]