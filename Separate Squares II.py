# 3454. Separate Squares II

# Hard

# You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

# Find the minimum y-coordinate value of a horizontal line such that the total area covered by squares above the line equals the total area covered by squares below the line.

# Answers within 10-5 of the actual answer will be accepted.

# Note: Squares may overlap. Overlapping areas should be counted only once in this version. 

# Example 1:

# Input: squares = [[0,0,1],[2,2,1]]

# Output: 1.00000

# Explanation:



# Any horizontal line between y = 1 and y = 2 results in an equal split, with 1 square unit above and 1 square unit below. The minimum y-value is 1.

# Example 2:

# Input: squares = [[0,0,2],[1,1,1]]

# Output: 1.00000

# Explanation:



# Since the blue square overlaps with the red square, it will not be counted again. Thus, the line y = 1 splits the squares into two equal parts.

 

# Constraints:

# 1 <= squares.length <= 5 * 104
# squares[i] = [xi, yi, li]
# squares[i].length == 3
# 0 <= xi, yi <= 109
# 1 <= li <= 109
# The total area of all the squares will not exceed 1015.

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))

        events.sort()
        xs = []
        prev_y = events[0][0]
        total = 0
        areas = []

        def union_len(intervals):
            intervals.sort()
            res = cur = 0
            end = -10**30
            for a, b in intervals:
                if a > end:
                    res += b - a
                    end = b
                elif b > end:
                    res += b - end
                    end = b
            return res

        for y, typ, x1, x2 in events:
            if y > prev_y and xs:
                h = y - prev_y
                w = union_len(xs)
                areas.append((prev_y, h, w))
                total += h * w
            if typ == 1:
                xs.append((x1, x2))
            else:
                xs.remove((x1, x2))
            prev_y = y

        half = total / 2
        acc = 0
        for y, h, w in areas:
            if acc + h * w >= half:
                return y + (half - acc) / w
            acc += h * w

        return 0.0