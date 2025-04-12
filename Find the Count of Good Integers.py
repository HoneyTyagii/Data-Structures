# 3272. Find the Count of Good Integers

# Hard

# You are given two positive integers n and k.
# An integer x is called k-palindromic if:
# x is a palindrome.
# x is divisible by k.
# An integer is called good if its digits can be rearranged to form a k-palindromic integer. For example, for k = 2, 2020 can be rearranged to form the k-palindromic integer 2002, whereas 1010 cannot be rearranged to form a k-palindromic integer.
# Return the count of good integers containing n digits.
# Note that any integer must not have leading zeros, neither before nor after rearrangement. For example, 1010 cannot be rearranged to form 101.

# Example 1:
# Input: n = 3, k = 5
# Output: 27
# Explanation:

# Some of the good integers are:

# 551 because it can be rearranged to form 515.
# 525 because it is already k-palindromic.
# Example 2:

# Input: n = 1, k = 4

# Output: 2

# Explanation:

# The two good integers are 4 and 8.

# Example 3:

# Input: n = 5, k = 6

# Output: 2468

# Constraints:

# 1 <= n <= 10
# 1 <= k <= 9


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        if n == 1: return 9//k
        k_pals, ans = set(), 0
        pals_left = product(*[digits[1:]]+[digits] *((n-1)//2)) 
        for pal_left in pals_left:
            pal_rght = pal_left[::-1][n%2:]                    
            pal = ''.join(((*pal_left, *pal_rght)))
            if int(pal)%k == 0:                                
                k_pals.add(''.join(sorted(pal)))
        for k_pal in k_pals:
            ctr = Counter(k_pal)                                
            denom = reduce(mul, map(factorial, ctr.values()))
            ans+= factorial(n)*(n - ctr['0'])//(denom * n)
        return ans