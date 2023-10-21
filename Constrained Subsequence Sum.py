# 1425. Constrained Subsequence Sum

# Hard

# Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

# A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

 

# Example 1:

# Input: nums = [10,2,-10,5,20], k = 2
# Output: 37
# Explanation: The subsequence is [10, 2, 5, 20].
# Example 2:

# Input: nums = [-1,-2,-3], k = 1
# Output: -1
# Explanation: The subsequence must be non-empty, so we choose the largest number.
# Example 3:

# Input: nums = [10,-2,-10,-5,20], k = 2
# Output: 23
# Explanation: The subsequence is [10, -2, -5, 20].
 

# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104

class Solution:
    def constrainedSubsetSum(self, nums, k):
        n = len(nums)
        dp, stack = [nums[0]] + [0]*(n-1), []
        for i in range(1,n):
            while stack and stack[0][1] + k < i:
                heappop(stack)
            heappush(stack,(-dp[i-1],i-1))
            dp[i] = max(0,-stack[0][0]) + nums[i]
        return max(dp)
    
    # time complexity: O(nlogn)
    # space complexity: O(n)