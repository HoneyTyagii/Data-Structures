# 2523. Closest Prime Numbers in Range

# Medium

# Given two positive integers left and right, find the two integers num1 and num2 such that:
# left <= num1 < num2 <= right .
# Both num1 and num2 are prime numbers.
# num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
# Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

# Example 1:

# Input: left = 10, right = 19
# Output: [11,13]
# Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
# The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
# Since 11 is smaller than 17, we return the first pair.

# Example 2:

# Input: left = 4, right = 6
# Output: [-1,-1]
# Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
 
# Constraints:

# 1 <= left <= right <= 106

class Solution:
    p = sorted({*range(2,1000001)}-{p*q for p in range(2,1001) for q in range(2,1000000//p+1)})
    def closestPrimes(self, l: int, r: int) -> List[int]:
        a = self.p[bisect_left(self.p,l):bisect_right(self.p,r)]
        return max(pairwise(a),key=lambda p:sub(*p),default=(-1,-1))