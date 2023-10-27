# 5. Longest Palindromic Substring

# Medium
# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = "" # varibale to store 
        resLen = 0 # len

        for i in range(len(s)):
            #odd lenght palindrome
            l, r = i, i #init left and right pointer at i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r-l+1) > resLen:
                    res = s[l:r +1] # update the longest palindrome
                    resLen = r - l + 1 # update the length of longest palindrome

                l -= 1
                r += 1

            l,r = i, i+1  #init left and right pointer at i and i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
        return res






        # def expand_around_center(left,right):
        #     while left >=0 and right < len(s) and s[left] == s[right]:
        #         left -= 1
        #         right += 1
        #     return s[left+1:right]

        # longest_palindrome = ""
        # for i in range(len(s)):
        #     odd_palindrome = expand_around_center(i,i)
        #     even_palindrome = expand_around_center(i, i+1)

        #     if len(odd_palindrome) > len(longest_palindrome):
        #         longest_palindrome = odd_palindrome
            
        #     if len(even_palindrome) > len(longest_palindrome):
        #         longest_palindrome = even_palindrome
        
        # return longest_palindrome



    #     n = len(s)
    #     longest_palindrome = "" # varibale to store

    #     #loop 
    #     for i in range(n):
    #         for j in range(i,n):
    #             substring = s[i:j+1] # extracting the values of substring i to j

    #             if isPalindrome(substring) and len(substring) > len(longest_palindrome):
    #                 longest_palindrome = substring
        
    #     return longest_palindrome
    
    # def isPalindrome(s):
    #     return s == s[::-1]

# Time complexity: O(N^3)
# Space complexity: O(1)