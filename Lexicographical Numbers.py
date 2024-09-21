# 386. Lexicographical Numbers

# Medium

# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

# You must write an algorithm that runs in O(n) time and uses O(1) extra space.  

# Example 1:

# Input: n = 13
# Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

# Example 2:

# Input: n = 2
# Output: [1,2] 

# Constraints:

# 1 <= n <= 5 * 104

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        output = []
        def dfs(curr):
            output.append(curr)
            if curr*10 <= n:
                dfs(curr*10)
            if curr+1 <= n and curr % 10 != 9:
                dfs(curr+1)   
        dfs(1)
        return output