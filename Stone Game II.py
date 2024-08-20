# 1140. Stone Game II

# Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

# Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

# On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

# The game continues until all the stones have been taken.

# Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

 

# Example 1:

# Input: piles = [2,7,9,4,4]
# Output: 10
# Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
# Example 2:

# Input: piles = [1,2,3,4,5,100]
# Output: 104
 

# Constraints:

# 1 <= piles.length <= 100
# 1 <= piles[i] <= 104

class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        suffix_sums = [0] * (n + 1)
        suffix_sums[n - 1] = piles[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + piles[i]

        dp = [[0] * (n + 1) for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                if i + 2 * m >= n:
                    dp[i][m] = suffix_sums[i]
                else:
                    for x in range(1, 2 * m + 1):
                        opponent_score = dp[i + x][max(x, m)]
                        score = suffix_sums[i] - opponent_score
                        dp[i][m] = max(dp[i][m], score)
        
        return dp[0][1]


# 2 approach
    
class Solution:
    def helper(self, piles, dp, suffixSum, i, M):
        if i == len(piles):
            return 0
        if i + 2 * M >= len(piles):
            return suffixSum[i]

        if dp[i][M] != 0:
            return dp[i][M]

        result = 0
        for x in range(1, 2 * M + 1):
            result = max(result, suffixSum[i] - self.helper(piles, dp, suffixSum, i + x, max(M, x)))

        dp[i][M] = result
        return result

    def stoneGameII(self, piles):
        if not piles:
            return 0
        dp = [[0] * len(piles) for _ in range(len(piles))]

        suffixSum = [0] * len(piles)
        suffixSum[-1] = piles[-1]
        for i in range(len(piles) - 2, -1, -1):
            suffixSum[i] = piles[i] + suffixSum[i + 1]

        return self.helper(piles, dp, suffixSum, 0, 1)