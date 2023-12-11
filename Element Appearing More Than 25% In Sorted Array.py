# 1287. Element Appearing More Than 25% In Sorted Array

# Easy

# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer. 

# Example 1:

# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6
# Example 2:

# Input: arr = [1,1]
# Output: 1
 

# Constraints:

# 1 <= arr.length <= 104
# 0 <= arr[i] <= 105

class Solution:
    def findSpecialInteger(self, A: List[int]) -> int:
        return collections.Counter(A).most_common(1)[0][0]