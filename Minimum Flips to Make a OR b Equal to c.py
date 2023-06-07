# 1318. Minimum Flips to Make a OR b Equal to c

# Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

 

# Example 1:



# Input: a = 2, b = 6, c = 5
# Output: 3
# Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
# Example 2:

# Input: a = 4, b = 2, c = 7
# Output: 1
# Example 3:

# Input: a = 1, b = 2, c = 3
# Output: 0
 

# Constraints:

# 1 <= a <= 10^9
# 1 <= b <= 10^9
# 1 <= c <= 10^9

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ba=bin(a)[2:]
        bb=bin(b)[2:]
        bc=bin(c)[2:]
        n=max(len(ba),len(bb),len(bc))
        ba="0"*(n-len(ba))+ba
        bb="0"*(n-len(bb))+bb
        bc="0"*(n-len(bc))+bc
        ct=0
        for i in range(n):
            if bc[i]=="0":
                if ba[i]=="1":
                    ct+=1
                if bb[i]=="1":
                    ct+=1
            else:
                if ba[i]=="1"or bb[i]=="1":
                    continue
                else:
                    ct+=1
        return ct