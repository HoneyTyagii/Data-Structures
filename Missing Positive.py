# 41. First Missing Positive


# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
# Example 3:

# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1

# Approach
# Initialize a set seen to store the numbers that have been seen in the array.

# Iterate through the array and add each number to the set seen.

# Initialize a variable i to 1.

# While i is less than or equal to the length of the array:
# If i is not in the set seen, return i.
# Otherwise, increment i by 1.

# Return i, as it is the first missing positive number.

# Complexity
# Time complexity: O(n)
# Space complexity: O(n)


#code

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
    # Initialize a set to store the numbers that have been seen
        seen = set()
    
    # Add each number to the set
        for num in nums:
            seen.add(num)
    
    # Initialize a variable to store the first missing positive number
        i = 1
    
    # While i is less than or equal to the length of the array
        while i <= len(nums):
        # If i is not in the set, return i
            if i not in seen:
                return i
        # Otherwise, increment i by 1
            else:
                i += 1
    
    # Return i, as it is the first missing positive number
        return i

