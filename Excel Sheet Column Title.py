# 168. Excel Sheet Column Title

# Easy

# 4.3K
# 597
# Companies
# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 

# Example 1:

# Input: columnNumber = 1
# Output: "A"
# Example 2:

# Input: columnNumber = 28
# Output: "AB"
# Example 3:

# Input: columnNumber = 701
# Output: "ZY"
 

# Constraints:

# 1 <= columnNumber <= 231 - 1

class Solution:
    def convertToTitle(self, num: int) -> str:
        ans=""
        while num > 0:
            num -= 1
            ans = chr(num % 26 + 65) + ans
            num //= 26
        return ans

        # time complexity: O(n)
        # space complexity: O(1)