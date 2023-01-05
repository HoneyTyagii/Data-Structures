# 452. Minimum Number of Arrows to Burst Balloons


# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

 

# Example 1:

# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
# - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
# Example 2:

# Input: points = [[1,2],[3,4],[5,6],[7,8]]
# Output: 4
# Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
# Example 3:

# Input: points = [[1,2],[2,3],[3,4],[4,5]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
# - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
 

# Constraints:

# 1 <= points.length <= 105
# points[i].length == 2
# -231 <= xstart < xend <= 231 - 1

#Approach
# To solve this problem, we can sort the balloons based on their xstart values, and then iterate through the sorted array. Whenever we encounter a balloon, we can check if the current arrow we are using can burst this balloon or not. If the arrow can burst the balloon, we don't need to use a new arrow and can move on to the next balloon. If the arrow cannot burst the current balloon, we will need to use a new arrow to burst it and set the x value of the current arrow to the xend value of the current balloon. We will also need to increment the number of arrows used in this case.

# Complexity Analysis

# Time Complexity: O(nlogn)
# Ap Complexity: O(1)

#code
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort the balloons by their xstart values
        points.sort(key=lambda x: x[0])
    
    # initialize the arrow to be at the negative infinity
        arrow = float("-inf")
    # initialize the number of arrows used to be 0
        arrows_used = 0

        for xstart, xend in points:
    # if the current arrow can't burst the current balloon, use a new arrow
            if arrow < xstart:
                arrows_used += 1
                arrow = xend
    # if the current arrow can burst the current balloon, move the arrow to the minimum
    # of its current position and the xend value of the current balloon 
            else:
                arrow = min(arrow, xend)
        return arrows_used