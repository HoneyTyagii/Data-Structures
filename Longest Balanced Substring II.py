# 3714. Longest Balanced Substring II

# Medium

# You are given a string s consisting only of the characters 'a', 'b', and 'c'.

# A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

# Return the length of the longest balanced substring of s.

# Example 1:

# Input: s = "abbac"

# Output: 4

# Explanation:

# The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

# Example 2:

# Input: s = "aabcc"

# Output: 3

# Explanation:

# The longest balanced substring is "abc" because all distinct characters 'a', 'b' and 'c' each appear exactly 1 time.

# Example 3:

# Input: s = "aba"

# Output: 2

# Explanation:

# One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".

 

# Constraints:

# 1 <= s.length <= 105
# s contains only the characters 'a', 'b', and 'c'.

class Solution:
    def longestBalanced(self, s: str) -> int:
        f, m, r = [0, 0, 0], {(i, 0, 0): 0 for i in range(4)}, max(sum(1 for _ in g) for _, g in groupby(s))
        for i, c in enumerate(s, 1):
            f[ord(c) - ord('a')] += 1
            r = max(r, i - m.setdefault((0, f[0]-f[1], f[1]-f[2]), i))
            r = max(r, i - m.setdefault((1, f[0]-f[1], f[2]), i))
            r = max(r, i - m.setdefault((2, f[1]-f[2], f[0]), i))
            r = max(r, i - m.setdefault((3, f[2]-f[0], f[1]), i))
        return r