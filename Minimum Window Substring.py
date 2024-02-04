# 76. Minimum Window Substring

# Hard

# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique. 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 
# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        def check(count1, count2):
            for key in count2:
                if count1[key] < count2[key]:
                        return False
            return True

        count2 = collections.Counter(t)
        count1 = collections.defaultdict(int)
        l = 0
        ans = ""
        n = float("inf")
        for r in range(len(s)):
            count1[s[r]] +=1
            while check(count1, count2) and l <= r:
                if r-l+1 <n:
                    ans = s[l:r+1]
                    n = r-l+1
                count1[s[l]] -=1
                l +=1
        return ans