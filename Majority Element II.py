# 229. Majority Element II

# Medium

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]
 
# Constraints:

# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)//3
        return [i for i in set(nums) if nums.count(i)>n]
    
    # time complexity : O(n)
    # space complexity : O(n)