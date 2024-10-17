# 670. Maximum Swap

# Medium

# You are given an integer num. You can swap two digits at most once to get the maximum valued number.

# Return the maximum valued number you can get.

# Example 1:

# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.

# Example 2:

# Input: num = 9973
# Output: 9973
# Explanation: No swap. 

# Constraints:

# 0 <= num <= 108

class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        ans = num[:]
        for i, p in enumerate(num):
            for j, q in enumerate(num[i+1:], start = i+1):
                if p < q:
                    n = num[:]
                    n[i], n[j] = q, p
                    if n > ans: ans = n
        return int(''.join(ans))