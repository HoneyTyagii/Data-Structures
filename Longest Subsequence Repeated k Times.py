# 2014. Longest Subsequence Repeated k Times

# Hard

# You are given a string s of length n, and an integer k. You are tasked to find the longest subsequence repeated k times in string s.
# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
# A subsequence seq is repeated k times in the string s if seq * k is a subsequence of s, where seq * k represents a string constructed by concatenating seq k times.
# For example, "bba" is repeated 2 times in the string "bababcba", because the string "bbabba", constructed by concatenating "bba" 2 times, is a subsequence of the string "bababcba".
# Return the longest subsequence repeated k times in string s. If multiple such subsequences are found, return the lexicographically largest one. If there is no such subsequence, return an empty string.

# Example 1:

# example 1
# Input: s = "letsleetcode", k = 2
# Output: "let"
# Explanation: There are two longest subsequences repeated 2 times: "let" and "ete".
# "let" is the lexicographically largest one.
# Example 2:

# Input: s = "bb", k = 2
# Output: "b"
# Explanation: The longest subsequence repeated 2 times is "b".
# Example 3:

# Input: s = "ab", k = 2
# Output: ""
# Explanation: There is no subsequence repeated 2 times. Empty string is returned.
 

# Constraints:

# n == s.length
# 2 <= n, k <= 2000
# 2 <= n < k * 8
# s consists of lowercase English letters.

from collections import Counter, deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def isKRepeatedSubsequence(s, t, k):
            pos = 0
            matched = 0
            for ch in s:
                if ch == t[pos]:
                    pos += 1
                    if pos == len(t):
                        matched += 1
                        if matched == k:
                            return True
                        pos = 0
            return False

        freq = Counter(s)
        valid = [ch for ch in sorted(freq.keys(), reverse=True) if freq[ch] >= k] 

        q = deque(valid) 
        ans = ""

        while q:
            curr = q.popleft()

            if len(curr) > len(ans) or (len(curr) == len(ans) and curr > ans):
                ans = curr

            for ch in valid:
                nxt = curr + ch
                if len(nxt) <= 7 and isKRepeatedSubsequence(s, nxt, k):
                    q.append(nxt)

        return ans