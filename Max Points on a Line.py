# 149. Max Points on a Line


# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

# Example 1:


# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3
# Example 2

# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
 
# Constraints:

# 1 <= points.length <= 300
# points[i].length == 2
# -104 <= xi,yi <= 104
# All the points are unique

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)<=2: return len(points)
        def line(p1,p2):
            if p2[0]-p1[0] == 0:
                return (p1[0])
            slope = (p2[1]-p1[1]) / (p2[0]-p1[0])                
            b = p1[1] - slope * p1[0]
            return (slope,"%.5f" % b)
        res = 0
        for i in range(len(points)):
            count = defaultdict(int)
            for j in range(i+1,len(points)):
                count[line(points[i],points[j])] += 1
            if count:
                res = max(res,max(count.values()))
        return res + 1