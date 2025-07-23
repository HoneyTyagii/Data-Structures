# 1717. Maximum Score From Removing Substrings

# Medium

# You are given a string s and two integers x and y. You can perform two types of operations any number of times.

# Remove substring "ab" and gain x points.
# For example, when removing "ab" from "cabxbae" it becomes "cxbae".
# Remove substring "ba" and gain y points.
# For example, when removing "ba" from "cabxbae" it becomes "cabxe".
# Return the maximum points you can gain after applying the above operations on s.

# Example 1:

# Input: s = "cdbcbbaaabab", x = 4, y = 5
# Output: 19
# Explanation:
# - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
# - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
# - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
# - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
# Total score = 5 + 4 + 5 + 5 = 19.

# Example 2:

# Input: s = "aabbaaxybbaabb", x = 5, y = 4
# Output: 20 

# Constraints:

# 1 <= s.length <= 105
# 1 <= x, y <= 104
# s consists of lowercase English letters.

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a, b = 'ab', 'ba'
        if y > x:
            b, a, y, x = a, b, x, y
        answer = 0
        
        for word in [a, b]:
            stack = []
            i = 0
            while i < len(s):
                stack.append(s[i])
                n = len(stack)
                prefix = stack[n-2] + stack[n-1]
                if prefix == word:
                    answer += x
                    stack.pop()
                    stack.pop()
                i += 1
            x = y
            
            s = ''.join(stack)
        return answer


# 2 Approach

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        for q,t in sorted(((x,'ab'),(y,'ba')))[::-1]:
            while t in s: res += q*(len(s)-len(s:=re.sub(t,'',s)))

        return res//2