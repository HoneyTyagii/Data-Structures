# 3321. Find X-Sum of All K-Long Subarrays II

# Hard

# You are given an array nums of n integers and two integers k and x.

# The x-sum of an array is calculated by the following procedure:

# Count the occurrences of all elements in the array.
# Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
# Calculate the sum of the resulting array.
# Note that if an array has less than x distinct elements, its x-sum is the sum of the array.

# Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].

# Example 1:

# Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2

# Output: [6,10,12]

# Explanation:

# For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence, answer[0] = 1 + 1 + 2 + 2.
# For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence, answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
# For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence, answer[2] = 2 + 2 + 2 + 3 + 3.
# Example 2:

# Input: nums = [3,8,7,8,7,5], k = 2, x = 2

# Output: [11,15,15,15,12]

# Explanation:

# Since k == x, answer[i] is equal to the sum of the subarray nums[i..i + k - 1].

# Constraints:

# nums.length == n
# 1 <= n <= 105
# 1 <= nums[i] <= 109
# 1 <= x <= k <= nums.length

from sortedcontainers import SortedSet
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        bottom=SortedSet()
        top=SortedSet()
        curr=0
        dic=defaultdict(int)
        ans=[]

        def update(ele,add):
            nonlocal curr

            if dic[ele]>0:
                if (dic[ele],ele) in bottom: bottom.remove((dic[ele],ele))
                else:
                    top.remove((dic[ele],ele))
                    curr-=dic[ele]*ele
            
            dic[ele]+=1 if add else -1
            if dic[ele]>0: bottom.add((dic[ele],ele))

        for i in range(len(nums)):
            update(nums[i],True)
            if i>=k: update(nums[i-k],False)

            while bottom and len(top)<x:
                cnt,ele=bottom.pop()
                curr+=ele*cnt
                top.add((cnt,ele))

            while bottom and bottom[-1]>top[0]:
                cntb,b=bottom.pop()
                cntt,t=top.pop(0)
                curr+=cntb*b
                curr-=cntt*t
                bottom.add((cntt,t))
                top.add((cntb,b))
            
            if i-k+1>=0: ans.append(curr)
        
        return ans