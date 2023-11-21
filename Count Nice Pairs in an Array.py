# 1814. Count Nice Pairs in an Array

# Medium

# You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

# 0 <= i < j < nums.length
# nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
# Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.

# Example 1:

# Input: nums = [42,11,1,97]
# Output: 2
# Explanation: The two pairs are:
#  - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
#  - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
# Example 2:

# Input: nums = [13,10,35,24,76]
# Output: 4 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:        
        n = len(nums)
        MOD = 10**9 + 7
        if n<=1:
            return 0
        def rev(i):
            new = 0
            while(i!=0):
                r = i%10
                new = new*10+r
                i = i//10
            return new
        freq_counter = defaultdict(int)
        for num in nums:
            freq_counter[num-rev(num)] += 1
        answer = 0
        for freq in freq_counter.keys():
            count = freq_counter[freq]
            answer = (answer + (count*(count-1))//2)%MOD                          
        return answer
    
# time complexity: O(NlogN), where N is the length of nums
# space complexity: O(N), where N is the length of nums