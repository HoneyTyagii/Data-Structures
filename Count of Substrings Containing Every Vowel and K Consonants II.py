# 3306. Count of Substrings Containing Every Vowel and K Consonants II

# Medium

# You are given a string word and a non-negative integer k.
# Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

# Example 1:

# Input: word = "aeioqq", k = 1

# Output: 0

# Explanation:

# There is no substring with every vowel.

# Example 2:

# Input: word = "aeiou", k = 0

# Output: 1

# Explanation:

# The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

# Example 3:

# Input: word = "ieaouqqieaouqq", k = 1

# Output: 3

# Explanation:

# The substrings with every vowel and one consonant are:

# word[0..5], which is "ieaouq".
# word[6..11], which is "qieaou".
# word[7..12], which is "ieaouq".
 

# Constraints:

# 5 <= word.length <= 2 * 105
# word consists only of lowercase English letters.
# 0 <= k <= word.length - 5

from collections import deque

class Solution:    
    def countOfSubstrings(self, word: str, k: int) -> int:
        def isCon(ch):
            return not (ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u")
        N = len(word)  
        vowel_pos = {"a": -1, "e": -1, "i": -1, "o": -1, "u": -1} 
        def leftest_vowel_pos():
            return min(vowel_pos.values())
        con_pos = deque()
        ans = 0
        con_cnt = 0
        for i in range(N):
            ch = word[i]
            if isCon(ch):
                con_pos.append(i)
                if len(con_pos) > k+1:
                    con_pos.popleft()
            else:
                vowel_pos[ch] = i
            
            leftest_vowel = leftest_vowel_pos()
            M = len(con_pos)
            if leftest_vowel >= 0: 
                if k == 0:
                    if M == 0:
                        ans += leftest_vowel + 1
                    else:
                        ans += max(0, leftest_vowel - con_pos[0])
                else:
                    if M == k+1:                        
                        con_posk1, con_posk = con_pos[0], con_pos[1]
                        leftest = min(leftest_vowel, con_posk)
                        ans += max(0, leftest - con_posk1)
                    elif M == k:                        
                        con_posk = con_pos[0]
                        leftest = min(leftest_vowel, con_posk)
                        ans += leftest + 1
        return ans