# 689. Maximum Sum of 3 Non-Overlapping Subarrays

# Hard

# Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

# Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

# Example 1:

# Input: nums = [1,2,1,2,6,7,5,1], k = 2
# Output: [0,3,5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
# Example 2:

# Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
# Output: [0,2,4] 

# Constraints:

# 1 <= nums.length <= 2 * 104
# 1 <= nums[i] < 216
# 1 <= k <= floor(nums.length / 3)

class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        sm1 = sm2 = sm3 = 0
        acc = list(accumulate(nums, initial = 0))
        for i, (a0,a1,a2,a3) in enumerate(zip(acc,acc[k:],acc[2*k:],acc[3*k:])):
            if a1 - a0 > sm1:
                sm1, idx1 = a1 - a0, i
            if a2 - a1 > sm2 - sm1:
                sm2, idx2 = sm1 + a2 - a1, (idx1, i+k)
            if a3 - a2 > sm3 - sm2:
                sm3, idx3 = sm2 + a3 - a2, (*idx2, i+2*k)
        return idx3