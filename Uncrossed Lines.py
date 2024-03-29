# 1035. Uncrossed Lines

# You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

# We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

# nums1[i] == nums2[j], and
# the line we draw does not intersect any other connecting (non-horizontal) line.
# Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

# Return the maximum number of connecting lines we can draw in this way.

 

# Example 1:


# Input: nums1 = [1,4,2], nums2 = [1,2,4]
# Output: 2
# Explanation: We can draw 2 uncrossed lines as in the diagram.
# We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.
# Example 2:

# Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
# Output: 3
# Example 3:

# Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
# Output: 2
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 500
# 1 <= nums1[i], nums2[j] <= 2000

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        if m == 0 or n == 0:
            return 0
        
        # Initialize a 2D array to store the maximum number of uncrossed lines
        max_lines = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    # If the current elements are equal, update the maximum number of uncrossed lines
                    max_lines[i][j] = max_lines[i - 1][j - 1] + 1
                else:
                    # If the current elements are not equal, take the maximum of the two previous elements
                    max_lines[i][j] = max(max_lines[i - 1][j], max_lines[i][j - 1])
        
        return max_lines[m][n]