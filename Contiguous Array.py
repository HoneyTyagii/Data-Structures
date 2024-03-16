# 525. Contiguous Array

# Medium

# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

# Example 1:

# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:

# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1. 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0:-1}                               
        count = 0                                  
        res = 0                                    
        for i in range(len(nums)):                 
            if nums[i] == 0:                        
                count -= 1
            if nums[i] == 1:
                count += 1
            if count in dic:                        
                res = max(res, i - dic[count])
            else:                                  
                dic[count] = i
        return res