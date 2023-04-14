# 516. Longest Palindromic Subsequence

# Given a string s, find the longest palindromic subsequence's length in s.

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
# Example 2:

# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".
 

# Constraints:

# 1 <= s.length <= 1000
# s consists only of lowercase English letters.

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for i in range(n-1, -1, -1):
            newdp = [0] * n
            newdp[i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    newdp[j] = 2 + dp[j-1]
                else:
                    newdp[j] = max(dp[j], newdp[j-1])
            dp = newdp
        return dp[-1]