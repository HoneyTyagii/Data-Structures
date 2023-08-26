# 646. Maximum Length of Pair Chain

# Medium

# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

# Return the length longest chain which can be formed.

# You do not need to use up all the given intervals. You can select pairs in any order.

# Example 1:

# Input: pairs = [[1,2],[2,3],[3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4].
# Example 2:

# Input: pairs = [[1,2],[7,8],[4,5]]
# Output: 3
# Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
 
# Constraints:

# n == pairs.length
# 1 <= n <= 1000
# -1000 <= lefti < righti <= 1000

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[0])
        n = len(pairs)
        dp = [1 for _ in range(n)]

        for i in reversed(range(n)):
            a, b = pairs[i]
            for j in range(i+1, n):
                if j == i: continue
                c, d = pairs[j]
                if b < c:
                    dp[i] = max(dp[i], 1+dp[j])
        return max(dp)
    
        # time complexity: O(n^2)
        # space complexity: O(n)