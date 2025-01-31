# 827. Making A Large Island

# Hard

# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
# Return the size of the largest island in grid after applying this operation.
# An island is a 4-directionally connected group of 1s.

# Example 1:

# Input: grid = [[1,0],[0,1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

# Example 2:

# Input: grid = [[1,1],[1,0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

# Example 3:

# Input: grid = [[1,1],[1,1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4. 

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 500
# grid[i][j] is either 0 or 1.

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def find(u):
            if u==parent[u]:
                return u
            else:
                parent[u]=find(parent[u])
                return parent[u]
        def union(u,v):
            pu,pv=find(u),find(v)
            if pu==pv:
                return 
            if size[pv]>size[pu]:
                parent[pu]=pv
                size[pv]+=size[pu]
            else:
                parent[pv]=pu
                size[pu]+=size[pv]
        
        n=len(grid)
        parent=[i for i in range(n*n)]
        size=[1 for i in range(n*n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    a=i*n+j
                    for u,v in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                        if 0<=u<n and 0<=v<n and grid[u][v]:
                            b=u*n+v
                            union(a,b)
        m=0 
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    t=set()
                    c=1
                    for u,v in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                        if 0<=u<n and 0<=v<n and grid[u][v]:
                            a=u*n+v
                            t.add(find(a))
                    for x in t:
                        c+=size[x]
                    if c>m:
                        m=c
        for i in range(n*n):
            m=max(m,size[find(i)])
        return m