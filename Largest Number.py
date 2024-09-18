# 179. Largest Number

# Medium

# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer. 

# Example 1:

# Input: nums = [10,2]
# Output: "210"

# Example 2:

# Input: nums = [3,30,34,5,9]
# Output: "9534330" 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 109

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        array = list(map(str, nums))
        array.sort(key=lambda x: x*10, reverse=True)        
        if array[0] == "0":
            return "0"        
        largest = ''.join(array)
        return largest