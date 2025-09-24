# 166. Fraction to Recurring Decimal

# Medium

# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.
# If multiple answers are possible, return any of them.
# It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

# Example 1:

# Input: numerator = 1, denominator = 2
# Output: "0.5"
# Example 2:

# Input: numerator = 2, denominator = 1
# Output: "2"
# Example 3:

# Input: numerator = 4, denominator = 333
# Output: "0.(012)" 

# Constraints:

# -231 <= numerator, denominator <= 231 - 1
# denominator != 0

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        curIndex = 0
        result = []
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            result.append("-")
            curIndex += 1
        numerator = abs(numerator)
        denominator = abs(denominator)

        quot, rem = divmod(numerator, denominator)
        if rem == 0:
            result.append(str(quot))
            return "".join(result)
        
        result.append(str(quot) + '.')
        curIndex += 1

        hmapQrRemindex = {}

        while rem != 0:
            rem *= 10
            quot, rem = divmod(rem, denominator)

            if (quot, rem) in hmapQrRemindex:
                index = hmapQrRemindex[(quot, rem)]
                result.insert(index, '(')
                result.append(")")
                break
            
            result.append(str(quot))
            hmapQrRemindex[quot, rem] = curIndex
            curIndex += 1
        
        return "".join(result)
