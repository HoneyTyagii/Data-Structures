# 1390. Four Divisors

# Medium

# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

# Example 1:

# Input: nums = [21,4,7]
# Output: 32
# Explanation: 
# 21 has 4 divisors: 1, 3, 7, 21
# 4 has 3 divisors: 1, 2, 4
# 7 has 2 divisors: 1, 7
# The answer is the sum of divisors of 21 only.
# Example 2:

# Input: nums = [21,21]
# Output: 64
# Example 3:

# Input: nums = [1,2,3,4,5]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 104
# 1 <= nums[i] <= 105

class Solution:
    def sumFourDivisors(self, nums):
        total_sum = 0

        for num in nums:
            divisor_count = 0
            divisor_sum = 0
            i = 1

            while i * i <= num:
                if num % i == 0:
                    d1 = i
                    d2 = num // i

                    divisor_count += 1
                    divisor_sum += d1

                    if d1 != d2:
                        divisor_count += 1
                        divisor_sum += d2

                    if divisor_count > 4:
                        break
                i += 1

            if divisor_count == 4:
                total_sum += divisor_sum

        return total_sum