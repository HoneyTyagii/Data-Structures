# 1493. Longest Subarray of 1's After Deleting One Element

# Medium

# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

# Example 1:

# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:

# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:

# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        zeros = 0
        ones = 0
        ans = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                ones += 1
            else:
                zeros += 1
            while zeros == 2:
                if nums[left] == 1:
                    ones -= 1
                else:
                    zeros -= 1
                left += 1
            if nums[right] == 0 and right + 1 < len(nums):
                ans = max(ans, ones + nums[right + 1])
            ans = max(ans, ones)

        return ans - 1 if ans == len(nums) else ans