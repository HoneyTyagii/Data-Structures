# 438. Find All Anagrams in a String

# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
 

# Constraints:

# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        LS, LP, S, P, A = len(s), len(p), 0, 0, []
        if LP > LS: 
            return []
        for i in range(LP): S, P = S + hash(s[i]), P + hash(p[i])
        if S == P: A.append(0)
        for i in range(LP, LS):
            S += hash(s[i]) - hash(s[i-LP])
            if S == P: A.append(i-LP+1)
        return A