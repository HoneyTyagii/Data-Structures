# 472. Concatenated Words

# Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

# A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

 

# Example 1:

# Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
# "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
# Example 2:

# Input: words = ["cat","dog","catdog"]
# Output: ["catdog"]
 

# Constraints:

# 1 <= words.length <= 104
# 1 <= words[i].length <= 30
# words[i] consists of only lowercase English letters.
# All the strings of words are unique.
# 1 <= sum(words[i].length) <= 105

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def can(w,dit):
            for i in range(mini,len(w)):
                lf=w[:i]  
                rt=w[i:]
                if lf in dit:
                    if rt in dit or can(rt,dit):
                        return True
        res=[]        
        dit = set(list(words))
        mini=10000
        for w in words:
            mini=min(len(w),mini)
        for w in words:
            if can(w,dit):
                res.append(w)
                
        return res