# 440. K-th Smallest in Lexicographical Order

# Hard
Extra Characters in a String
# Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n]. 

# Example 1:

# Input: n = 13, k = 2
# Output: 10
# Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.

# Example 2:

# Input: n = 1, k = 1
# Output: 1 

# Constraints:

# 1 <= k <= n <= 109

class Solution:
    def findKthNumber(self, n, k):
        current_prefix = 1
        k -= 1
        
        while k > 0:
            count = self.countNumbersWithPrefix(current_prefix, n)
            if k >= count:
                current_prefix += 1
                k -= count
            else:
                current_prefix *= 10
                k -= 1
        
        return current_prefix

    def countNumbersWithPrefix(self, prefix, n):
        first_number = prefix
        next_number = prefix + 1
        total_count = 0

        while first_number <= n:
            total_count += min(n + 1, next_number) - first_number
            first_number *= 10
            next_number *= 10

        return total_count


# 2 Aprroach

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def countSteps(prefix, n):
            steps = 0
            current = prefix
            next_prefix = prefix + 1
            while current <= n:
                steps += min(n + 1, next_prefix) - current
                current *= 10
                next_prefix *= 10
            return steps
        current = 1
        k -= 1
        while k > 0:
            steps = countSteps(current, n)
            if steps <= k:
                current += 1
                k -= steps
            else:
                current *= 10
                k -= 1
        return current