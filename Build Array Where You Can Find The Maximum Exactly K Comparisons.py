# 1420. Build Array Where You Can Find The Maximum Exactly K Comparisons

# Hard

# You are given three integers n, m and k. Consider the following algorithm to find the maximum element of an array of positive integers:


# You should build the array arr which has the following properties:

# arr has exactly n integers.
# 1 <= arr[i] <= m where (0 <= i < n).
# After applying the mentioned algorithm to arr, the value search_cost is equal to k.
# Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 109 + 7.

 

# Example 1:

# Input: n = 2, m = 3, k = 1
# Output: 6
# Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
# Example 2:

# Input: n = 5, m = 2, k = 3
# Output: 0
# Explanation: There are no possible arrays that satisify the mentioned conditions.
# Example 3:

# Input: n = 9, m = 1, k = 1
# Output: 1
# Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]
 

# Constraints:

# 1 <= n <= 50
# 1 <= m <= 100
# 0 <= k <= n

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = {}
        
        def helper(curr_max, n,k):
            if k==0:
                return (curr_max ** n)%MOD
            
            if n==0:
                return 0
            
            if (curr_max, n,k) in dp:
                return dp[(curr_max, n,k)]
            
            a = 0
            for val in range(1,m+1):
                temp = k
                if curr_max < val:
                    temp-=1
                a = (a + helper(max(curr_max, val),n-1,temp))%MOD
            dp[(curr_max, n,k)] = a
            return dp[(curr_max, n,k)]
        return helper(0,n,k)%MOD
            
# time complexity : O(n*m*k)
# space complexity : O(n*m*k)