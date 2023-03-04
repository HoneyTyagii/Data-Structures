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
             

# Approach 
 
# If the string is empty, return True. 

# If the string has only one character, return True. 
 
# If the first character is uppercase and the rest of the characters are lowercase, return True. 

# If the first character is lowercase and the rest of the characters are uppercase, return False.  
 
# If the first character is uppercase and the rest of the characters are uppercase, return True.  

# If the first character is lowercase and the rest of the characters are lowercase, return True.  

# Complexity 
# Time complexity: O(n)  
# Space complexity: O(1)   

#code

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
    # If the string is empty or has only one character, return True
        if len(word) <= 1:
            return True
    
    # If the first character is uppercase and the rest of the characters are lowercase, return True
        if word[0].isupper() and word[1:].islower():
            return True
    
    # If the first character is lowercase and the rest of the characters are uppercase, return False
        if word[0].islower() and word[1:].isupper():
            return False
    
    # If the first character is uppercase and the rest of the characters are uppercase, return True
        if word[0].isupper() and word[1:].isupper():
            return True
    
    # If the first character is lowercase and the rest of the characters are lowercase, return True
        if word[0].islower() and word[1:].islower():
            return True
