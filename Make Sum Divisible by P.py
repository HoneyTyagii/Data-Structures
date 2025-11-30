# 1590. Make Sum Divisible by P

# Medium

# Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

# Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

# A subarray is defined as a contiguous block of elements in the array. 

# Example 1:

# Input: nums = [3,1,4,2], p = 6
# Output: 1
# Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.

# Example 2:

# Input: nums = [6,3,5,2], p = 9
# Output: 2
# Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.

# Example 3:

# Input: nums = [1,2,3], p = 3
# Output: 0
# Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything. 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= p <= 109

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if sum(nums)%p==0:
            return 0
        target = sum(nums) % p
        dic,n = {0:-1},len(nums)
        cur,ret = 0,n
        for i,num in enumerate(nums):
            cur = (cur+num)%p
            if dic.get((cur-target)%p) is not None:
                ret = min(ret,i-dic.get((cur-target)%p))
            dic[cur] = i
        return ret if ret < n else -1
    
# 2 Approach

class Solution:
    def minSubarray(self, A, p):
        need = sum(A) % p
        if need == 0:
            return 0

        mp = {0: -1}   
        cur = 0
        res = n = len(A)

        for i, a in enumerate(A):
            cur = (cur + a) % p
            target = (cur - need) % p
            if target in mp:
                res = min(res, i - mp[target])
            
            mp[cur] = i

        return res if res < n else -1