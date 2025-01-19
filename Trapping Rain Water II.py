# 407. Trapping Rain Water II

# Hard

# Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

# Example 1:

# Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# Output: 4
# Explanation: After the rain, water is trapped between the blocks.
# We have two small ponds 1 and 3 units trapped.
# The total volume of water trapped is 4.

# Example 2:

# Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
# Output: 10
 
# Constraints:

# m == heightMap.length
# n == heightMap[i].length
# 1 <= m, n <= 200
# 0 <= heightMap[i][j] <= 2 * 10^4

import heapq
class Solution:
    def trapRainWater(self, h: List[List[int]]) -> int:
            
        q=[]
        heapq.heapify(q)
        visited=set()
        
        def isValid(m,n):
            if 0<=m<r and 0<=n<c:
                return True
            return False
        
        r=len(h)
        c=len(h[0])
        
        for i in range(r):
            for j in range(c):
                if i==0 or i==r-1 or j==0 or j==c-1:
                    heapq.heappush(q,(h[i][j],i,j))
                    visited.add((i,j))
        res=0
        while q:
            cur=heapq.heappop(q)
            
            for d in [(-1,0),(1,0),(0,-1),(0,1)]:
                new_i=cur[1]+d[0]
                new_j = cur[2]+d[1]
                if isValid(new_i, new_j) and (new_i, new_j) not in visited:
                    h_inc=max(0,cur[0]-h[new_i][new_j])
                    res+=h_inc
                    if h_inc>0:
                        heapq.heappush(q,(cur[0],new_i, new_j))
                    else:
                         heapq.heappush(q,(h[new_i][new_j],new_i, new_j))
                    visited.add((new_i, new_j))
        return res