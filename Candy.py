# 135. Candy

# Hard

# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

 

# Example 1:

# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Example 2:

# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.
 

# Constraints:

# n == ratings.length
# 1 <= n <= 2 * 104
# 0 <= ratings[i] <= 2 * 104

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        temp = [1]*n
        
        for i in range(1,n):
            if(ratings[i]>ratings[i-1]):
                temp[i]=temp[i-1]+1
        if(n>1):
            if(ratings[0]>ratings[1]):
                temp[0]=2
                
            
        for i in range(n-2,-1,-1):
            if(ratings[i]>ratings[i+1] and temp[i]<=temp[i+1]):
                temp[i]=temp[i+1]+1

                
        return sum(temp)
    
# time complexity : O(n)
# space complexity : O(n)

# 2 Approach
    
class Solution:
    def candy(self, a: List[int]) -> int:
        f = lambda a:[*accumulate(map(lt,a,a[1:]),lambda q,p:q*p+1,initial=1)]
        return sum(map(max,f(a),f(a[::-1])[::-1]))