# 1092. Shortest Common Supersequence 

# Hard

# Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.
# A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

# Example 1:

# Input: str1 = "abac", str2 = "cab"
# Output: "cabac"
# Explanation: 
# str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
# str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
# The answer provided is the shortest such string that satisfies these properties.

# Example 2:

# Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
# Output: "aaaaaaaa" 

# Constraints:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of lowercase English letters.

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n1 , n2 = len(str1) , len(str2)
        pre = [""] * (n2+1)
        for i in range(1,(n1+1)):
            cur = [""] * (n2+1)
            for j in range(1,(n2+1)):
                if str1[i-1] == str2[j-1]:
                    cur[j] = pre[j-1] + str1[i-1]
                else:
                    if len(pre[j])  >= len(cur[j-1]):
                        cur[j] = pre[j]
                    else:
                        cur[j] = cur[j-1]
            pre = cur[:]
        lcs = pre[-1]
        ans = ""
        i , j = 0 , 0
        for cur in pre[-1] + "@":
            while i < len(str1) and str1[i] != cur:
                ans += str1[i]
                i += 1
            while j < len(str2) and str2[j] != cur:
                ans += str2[j]
                j += 1
            i += 1
            j += 1
            ans += cur
        return ans[:-1]