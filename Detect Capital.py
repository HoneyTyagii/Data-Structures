# 520. Detect Capital

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

 

# Example 1:

# Input: word = "USA"
# Output: true
# Example 2:

# Input: word = "FlaG"
# Output: false
 

# Constraints:

# 1 <= word.length <= 100
# word consists of lowercase and uppercase English letters.


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 1:
            return True
        if word[0].isupper() and word[1:].islower():
            return True
        if word[0].islower() and word[1:].isupper():
            return False
        if word[0].isupper() and word[1:].isupper():
            return True
        if word[0].islower() and word[1:].islower():
            return True