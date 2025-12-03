# 3625. Count Number of Trapezoids II

# Hard

# You are given a 2D integer array points where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

# Return the number of unique trapezoids that can be formed by choosing any four distinct points from points.

# A trapezoid is a convex quadrilateral with at least one pair of parallel sides. Two lines are parallel if and only if they have the same slope.

# Example 1:

# Input: points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]

# Output: 2

# Explanation:



# There are two distinct ways to pick four points that form a trapezoid:

# The points [-3,2], [2,3], [3,2], [2,-3] form one trapezoid.
# The points [2,3], [3,2], [3,0], [2,-3] form another trapezoid.
# Example 2:

# Input: points = [[0,0],[1,0],[0,1],[2,1]]

# Output: 1

# Explanation:



# There is only one trapezoid which can be formed.

 

# Constraints:

# 4 <= points.length <= 500
# –1000 <= xi, yi <= 1000
# All points are pairwise distinct.

class Solution:   
    def countTrapezoids(self, P):
        from collections import defaultdict
        ans, n = 0, len(P)
        S2I = defaultdict(list)
        M2S = defaultdict(list)

        for i in range(n):
            x1, y1 = P[i]
            for j in range(i + 1, n):
                x2, y2 = P[j]
                dx, dy = x1 - x2, y1 - y2
                if x1 == x2: k, b = inf, x1
                else:
                    k = (y2 - y1) / (x2 - x1)
                    b = (y1 * dx - x1 * dy) / dx
                mid = (x1 + x2) * 10000 + (y1 + y2)
                S2I[k].append(b) ; M2S[mid].append(k)

        for arr in (S2I, M2S):
            for v in arr.values():
                if len(v) < 2: continue
                c, s = defaultdict(int), 0
                for x in v: c[x] += 1
                for t in c.values():
                    ans += s*t if arr is S2I else -s*t
                    s += t
        return ans