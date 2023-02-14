# 67. Add Binary

# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize the result string and the carry value
        result = ""
        carry = 0
        # Convert the input strings to lists of digits
        a = list(a)
        b = list(b)
        # Loop until both lists are empty or the carry is nonzero
        while a or b or carry:
            # Pop the rightmost digits from the lists, or use zero if empty
            x = int(a.pop()) if a else 0
            y = int(b.pop()) if b else 0
            # Add the digits and the carry, and update the carry
            sum = x + y + carry
            carry = sum // 2
            # Append the remainder to the result string
            result = str(sum % 2) + result
        # Return the result string
        return result