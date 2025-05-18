# 1931. Painting a Grid With Three Different Colors

# Hard

# You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.
# Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 109 + 7.

# Example 1:

# Input: m = 1, n = 1
# Output: 3
# Explanation: The three possible colorings are shown in the image above.

# Example 2:

# Input: m = 1, n = 2
# Output: 6
# Explanation: The six possible colorings are shown in the image above.

# Example 3:

# Input: m = 5, n = 5
# Output: 580986
 
# Constraints:

# 1 <= m <= 5
# 1 <= n <= 1000

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        C = reduce(
            lambda C, _: [c + [(c[-1] + d) % 3] for c in C for d in range(1, 3)],
            range(m - 1),
            [[i] for i in range(3)])
        M = [
            [j for j in range(len(C)) if all(a != b for a, b in zip(c1, C[j]))]
            for c1 in C]
        return sum(reduce(
            lambda res, _: [sum(res[c] for c in row) % 1_000_000_007 for row in M],
            range(n - 1),
            [1] * len(C))) % 1_000_000_007