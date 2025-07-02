# 3333. Find the Original Typed String II

# Hard

# Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

# You are given a string word, which represents the final output displayed on Alice's screen. You are also given a positive integer k.

# Return the total number of possible original strings that Alice might have intended to type, if she was trying to type a string of size at least k.

# Since the answer may be very large, return it modulo 109 + 7. 

# Example 1:

# Input: word = "aabbccdd", k = 7

# Output: 5

# Explanation:

# The possible strings are: "aabbccdd", "aabbccd", "aabbcdd", "aabccdd", and "abbccdd".

# Example 2:

# Input: word = "aabbccdd", k = 8

# Output: 1

# Explanation:

# The only possible string is "aabbccdd".

# Example 3:

# Input: word = "aaabbb", k = 3

# Output: 8

 

# Constraints:

# 1 <= word.length <= 5 * 105
# word consists only of lowercase English letters.
1 <= k <= 2000

from functools import reduce
from itertools import accumulate

m = 10**9 + 7
mul = lambda a, b: a * b % m
add = lambda a, b: (a + b) % m
sub = lambda a, b: (a - b + m) % m

class Solution:
    def possibleStringCount(self, w: str, k: int) -> int:
        s = [1]
        for i in range(1, len(w)):
            if w[i] != w[i-1]:
                s.append(1)
            else:
                s[-1] += 1
        t = reduce(mul, s)
        if k <= len(s):
            return t
        dp = [1] + [0] * (k - 1)
        for i in range(1, len(s) + 1):
            pre = list(accumulate(dp, add, initial=0))
            dp2 = [0] * k
            for j in range(i, k):
                l = min(s[i - 1], j - i + 1)
                dp2[j] = sub(pre[j], pre[j - l])
            dp = dp2
        return sub(t, sum(dp) % m)