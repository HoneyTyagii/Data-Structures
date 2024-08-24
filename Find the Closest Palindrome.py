# 564. Find the Closest Palindrome

# Hard

# Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

# The closest is defined as the absolute difference minimized between two integers. 

# Example 1:

# Input: n = "123"
# Output: "121"

# Example 2:

# Input: n = "1"
# Output: "0"
# Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0. 

# Constraints:

# 1 <= n.length <= 18
# n consists of only digits.
# n does not have leading zeros.
# n is representing an integer in the range [1, 1018 - 1].

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        return (l:=len(n),p:=int(n[:(l+1)//2])) and str(min({10**(l-1)-1,10**l+1,*(int((t:=str(p+q))+t[-1-l%2::-1]) for q in (-1,0,1))}-{n:=int(n)},key=lambda v:(abs(v-n),v)))