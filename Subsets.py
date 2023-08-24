# 78. Subsets

# Medium

# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = [[]]
        num_len = len(nums)
        for n in range(num_len):
            counter = 0
            len_power_set = len(power_set)
            for subset in power_set:
                NewSubset = subset + [nums[n]]
                power_set.append(NewSubset)
                counter += 1
                if counter >= len_power_set:
                    break
        return power_set
    
        # time complexity: O(n^2)
        # space complexity: O(n^2)