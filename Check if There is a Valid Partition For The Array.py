# 2369. Check if There is a Valid Partition For The Array

# Medium

# You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

# We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

# The subarray consists of exactly 2 equal elements. For example, the subarray [2,2] is good.
# The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.
# The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
# Return true if the array has at least one valid partition. Otherwise, return false.

# Example 1:

# Input: nums = [4,4,4,5,6]
# Output: true
# Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
# This partition is valid, so we return true.
# Example 2:

# Input: nums = [1,1,1,2]
# Output: false
# Explanation: There is no valid partition for this array.
 

# Constraints:

# 2 <= nums.length <= 105
# 1 <= nums[i] <= 106

class Solution:
    def validPartition(self, n: List[int]) -> bool:
        dp = [False] * len(n)
        if n[1] == n[0]:
            dp[1] = True
        if len(n) == 2:
            return dp[-1]
        if (n[0] == n[1] == n[2]) or (n[0] + 2 == n[1] + 1 == n[2]):
            dp[2] = True
        for i in range(3,len(n)):
            condition_one = n[i] == n[i - 1]
            condition_two_three = (condition_one and n[i] == n[i - 2]) or (n[i] - 1 == n[i - 1] and n[i] - 2 == n[i - 2])
            dp[i] = (dp[i - 2] and condition_one) or (dp[i - 3] and condition_two_three)
        return dp[-1]
    
    # time complexity: O(n)
    # space complexity: O(n)