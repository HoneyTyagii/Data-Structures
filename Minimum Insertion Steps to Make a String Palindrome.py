# 1312. Minimum Insertion Steps to Make a String Palindrome

# Given a string s. In one step you can insert any character at any index of the string.

# Return the minimum number of steps to make s palindrome.

# A Palindrome String is one that reads the same backward as well as forward.

 

# Example 1:

# Input: s = "zzazz"
# Output: 0
# Explanation: The string "zzazz" is already palindrome we do not need any insertions.
# Example 2:

# Input: s = "mbadm"
# Output: 2
# Explanation: String can be "mbdadbm" or "mdbabdm".
# Example 3:

# Input: s = "leetcode"
# Output: 5
# Explanation: Inserting 5 characters the string becomes "leetcodocteel".
 

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for i in range(n - 2, -1, -1):
            prev = 0
            for j in range(i + 1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = prev
                else:
                    dp[j] = min(dp[j], dp[j-1]) + 1
                prev = temp
        return dp[n-1]