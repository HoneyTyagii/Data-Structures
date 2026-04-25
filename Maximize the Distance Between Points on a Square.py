# 3464. Maximize the Distance Between Points on a Square

# Hard

# You are given an integer side, representing the edge length of a square with corners at (0, 0), (0, side), (side, 0), and (side, side) on a Cartesian plane.

# You are also given a positive integer k and a 2D integer array points, where points[i] = [xi, yi] represents the coordinate of a point lying on the boundary of the square.

# You need to select k elements among points such that the minimum Manhattan distance between any two points is maximized.

# Return the maximum possible minimum Manhattan distance between the selected k points.

# The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.

 

# Example 1:

# Input: side = 2, points = [[0,2],[2,0],[2,2],[0,0]], k = 4

# Output: 2

# Explanation:



# Select all four points.

# Example 2:

# Input: side = 2, points = [[0,0],[1,2],[2,0],[2,2],[2,1]], k = 4

# Output: 1

# Explanation:



# Select the points (0, 0), (2, 0), (2, 2), and (2, 1).

# Example 3:

# Input: side = 2, points = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]], k = 5

# Output: 1

# Explanation:



# Select the points (0, 0), (0, 1), (0, 2), (1, 2), and (2, 2).

 

# Constraints:

# 1 <= side <= 109
# 4 <= points.length <= min(4 * side, 15 * 103)
# points[i] == [xi, yi]
# The input is generated such that:
# points[i] lies on the boundary of the square.
# All points[i] are unique.
# 4 <= k <= min(25, points.length)

class Solution: # Time = O(n log n + nk log side) = O(n * log(n * side ^ k))
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        arr = list()                # Space = O(n + k)
        for x, y in points:
            if x == 0: arr.append(y)
            elif y == side: arr.append(side + x)
            elif x == side: arr.append(side * 3 - y)
            else: arr.append(side * 4 - x)
        arr.sort()

        def check(low: int) -> bool:
            idx, cur = [0] * k, arr[0]
            for j in range(1, k):
                i = bisect_left(arr, cur + low)
                if i == len(arr): return False
                idx[j], cur = i, arr[i]
            if cur - arr[0] <= side * 4 - low: return True

            for idx[0] in range(1, idx[1]):
                for j in range(1, k):
                    while arr[idx[j]] < arr[idx[j - 1]] + low:
                        idx[j] += 1
                        if idx[j] == len(arr): return False
                if arr[idx[-1]] - arr[idx[0]] <= side * 4 - low: return True
            return False

        left, right = 1, side + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid): left = mid
            else: right = mid
        return left