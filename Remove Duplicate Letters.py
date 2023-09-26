# 316. Remove Duplicate Letters

# Medium

# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
# the smallest in lexicographical order
#  among all possible results.

# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb" 

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        for i, char in enumerate(s):
            if char in stack:
                continue
                
            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                stack.pop()
                
            stack.append(char)
            
        return ''.join(stack)
    
#         time complexity: O(n)
#         space complexity: O(n)