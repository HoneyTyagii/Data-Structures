# 3097. Shortest Subarray With OR at Least K II

# Medium

# You are given an array nums of non-negative integers and an integer k.

# An array is called special if the bitwise OR of all of its elements is at least k.

# Return the length of the shortest special non-empty 
# subarray
#  of nums, or return -1 if no special subarray exists. 

# Example 1:

# Input: nums = [1,2,3], k = 2

# Output: 1

# Explanation:

# The subarray [3] has OR value of 3. Hence, we return 1.

# Example 2:

# Input: nums = [2,1,8], k = 10

# Output: 3

# Explanation:

# The subarray [2,1,8] has OR value of 11. Hence, we return 3.

# Example 3:

# Input: nums = [1,2], k = 0

# Output: 1

# Explanation:

# The subarray [1] has OR value of 1. Hence, we return 1.

# Constraints:

# 1 <= nums.length <= 2 * 105
# 0 <= nums[i] <= 109
# 0 <= k <= 109

class Solution:
    def minimumSubarrayLength(self, a: List[int], k: int) -> int:
        res, z, p1 = inf, Counter(), 0
        for p2 in range(len(a)):
            z.update(i for i,c in enumerate(bin(a[p2])[:1:-1]) if c=='1')
            while p1<=p2 and sum(1<<i for i,f in z.items() if f)>=k:
                res = min(res, p2-p1+1)
                z.update({i:-1 for i,c in enumerate(bin(a[p1])[:1:-1]) if c=='1'})
                p1 += 1
        return res==inf and -1 or res