# 1888. Minimum Number of Flips to Make the Binary String Alternating

# Medium

# You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

# Type-1: Remove the character at the start of the string s and append it to the end of the string.
# Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
# Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

# The string is called alternating if no two adjacent characters are equal.

# For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
 

# Example 1:

# Input: s = "111000"
# Output: 2
# Explanation: Use the first operation two times to make s = "100011".
# Then, use the second operation on the third and sixth elements to make s = "101010".
# Example 2:

# Input: s = "010"
# Output: 0
# Explanation: The string is already alternating.
# Example 3:

# Input: s = "1110"
# Output: 1
# Explanation: Use the second operation on the second element to make s = "1010".
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either '0' or '1'.

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        cnts = [0, 0]
        for i in range(n):
            if s[i] == '0':
                cnts[i % 2] += 1
        
        even_tot = (n+1) // 2
        odd_tot = n // 2
        ans = n
        for i in range(n):
            even_zeros = cnts[0]
            even_ones = even_tot - cnts[0]
            odd_zeros = cnts[1]
            odd_ones = odd_tot - cnts[1]

            zcnt = even_ones + odd_zeros
            ocnt = even_zeros + odd_ones
            ans = min(ans, zcnt, ocnt)

            cnts[0], cnts[1] = cnts[1], cnts[0]
            
            if n % 2 and s[i] == '0':
                cnts[0] += 1
                cnts[1] -= 1

        return ans