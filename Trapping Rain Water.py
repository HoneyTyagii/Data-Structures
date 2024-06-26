# 42. Trapping Rain Water

# Hard

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining. 

# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

class Solution:
    def trap(self, height: List[int]) -> int:
        mh = max(height)
        block_vol = sum(height)

        left = 0
        max_left = 0
        while height[left] < mh:
            if height[left] > max_left:
                max_left = height[left]
            
            height[left] = max_left
            left += 1
        
        right = len(height)-1
        max_right = 0
        while height[right] < mh:
            if height[right] > max_right:
                max_right = height[right]
            
            height[right] = max_right
            right -= 1
        
        filled_vol = sum(height[0:left]+height[right:]) + (right-left)*mh
        return filled_vol - block_vol