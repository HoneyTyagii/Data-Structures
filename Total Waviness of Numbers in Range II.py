# 3753. Total Waviness of Numbers in Range II

# Hard

# You are given two integers num1 and num2 representing an inclusive range [num1, num2].

# The waviness of a number is defined as the total count of its peaks and valleys:

# A digit is a peak if it is strictly greater than both of its immediate neighbors.
# A digit is a valley if it is strictly less than both of its immediate neighbors.
# The first and last digits of a number cannot be peaks or valleys.
# Any number with fewer than 3 digits has a waviness of 0.
# Return the total sum of waviness for all numbers in the range [num1, num2].
 

# Example 1:

# Input: num1 = 120, num2 = 130

# Output: 3

# Explanation:

# In the range [120, 130]:

# 120: middle digit 2 is a peak, waviness = 1.
# 121: middle digit 2 is a peak, waviness = 1.
# 130: middle digit 3 is a peak, waviness = 1.
# All other numbers in the range have a waviness of 0.
# Thus, total waviness is 1 + 1 + 1 = 3.

# Example 2:

# Input: num1 = 198, num2 = 202

# Output: 3

# Explanation:

# In the range [198, 202]:

# 198: middle digit 9 is a peak, waviness = 1.
# 201: middle digit 0 is a valley, waviness = 1.
# 202: middle digit 0 is a valley, waviness = 1.
# All other numbers in the range have a waviness of 0.
# Thus, total waviness is 1 + 1 + 1 = 3.

# Example 3:

# Input: num1 = 4848, num2 = 4848

# Output: 2

# Explanation:

# Number 4848: the second digit 8 is a peak, and the third digit 4 is a valley, giving a waviness of 2.

 

# Constraints:

# 1 <= num1 <= num2 <= 1015​​​​​​​

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        wav=[l*100+m*10+r for l,m,r in product(range(10),range(10),range(10)) if l<m>r or l>m<r]
        i100 = bisect_left(wav,100)
        def waves(n):
            ans,suf,pow = 0,0,1
            while  n >= 100:
                prf,win = n//1000, n%1000
                idx  = bisect_left(wav, win)
                eq   = idx < len(wav) and wav[idx] == win
                nlt1 = min(idx, i100)
                nlt0 = max(0, idx-i100)
                nge1 = max(0, i100-idx)
                nge0 = min(len(wav)-idx, len(wav)-i100)
                ans += (nlt1*prf + nlt0*(prf+1) + nge0*prf + nge1*max(0,prf-1))*pow + eq*(suf+1)
                suf += n%10 *pow
                n //= 10; pow *= 10
            return  ans
        return  waves(num2) - waves(num1 -1)
        