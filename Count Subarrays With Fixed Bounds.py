# 2444. Count Subarrays With Fixed Bounds

# Hard

# You are given an integer array nums and two integers minK and maxK.
# A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

# The minimum value in the subarray is equal to minK.
# The maximum value in the subarray is equal to maxK.
# Return the number of fixed-bound subarrays.

# A subarray is a contiguous part of an array.

# Example 1:

# Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# Output: 2
# Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
# Example 2:

# Input: nums = [1,1,1,1], minK = 1, maxK = 1
# Output: 10
# Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.

# Constraints:

# 2 <= nums.length <= 105
# 1 <= nums[i], minK, maxK <= 106

class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        div, minLast, maxLast = 0, -1, -1
        res = 0
        for i, num in enumerate(nums):
            if not (minK <= num <= maxK):
                div, minLast, maxLast = i + 1, -1, -1
                continue
            minLast, maxLast = (
                i if num == minK else minLast,
                i if num == maxK else maxLast,
            )
            res += (
                min(maxLast, minLast) - div + 1
                if minLast != -1 and maxLast != -1
                else 0
            )
        return res