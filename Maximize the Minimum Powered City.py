# 2528. Maximize the Minimum Powered City

# Hard

# You are given a 0-indexed integer array stations of length n, where stations[i] represents the number of power stations in the ith city.

# Each power station can provide power to every city in a fixed range. In other words, if the range is denoted by r, then a power station at city i can provide power to all cities j such that |i - j| <= r and 0 <= i, j <= n - 1.

# Note that |x| denotes absolute value. For example, |7 - 5| = 2 and |3 - 10| = 7.
# The power of a city is the total number of power stations it is being provided power from.

# The government has sanctioned building k more power stations, each of which can be built in any city, and have the same range as the pre-existing ones.

# Given the two integers r and k, return the maximum possible minimum power of a city, if the additional power stations are built optimally.

# Note that you can build the k power stations in multiple cities.

# Example 1:

# Input: stations = [1,2,4,5,0], r = 1, k = 2
# Output: 5
# Explanation: 
# One of the optimal ways is to install both the power stations at city 1. 
# So stations will become [1,4,4,5,0].
# - City 0 is provided by 1 + 4 = 5 power stations.
# - City 1 is provided by 1 + 4 + 4 = 9 power stations.
# - City 2 is provided by 4 + 4 + 5 = 13 power stations.
# - City 3 is provided by 5 + 4 = 9 power stations.
# - City 4 is provided by 5 + 0 = 5 power stations.
# So the minimum power of a city is 5.
# Since it is not possible to obtain a larger power, we return 5.
# Example 2:

# Input: stations = [4,4,4,4], r = 0, k = 3
# Output: 4
# Explanation: 
# It can be proved that we cannot make the minimum power of a city greater than 4.
 
# Constraints:

# n == stations.length
# 1 <= n <= 105
# 0 <= stations[i] <= 105
# 0 <= r <= n - 1
# 0 <= k <= 109

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        pref_sum, power = [0] * n, [0] * n
        pref_sum[0] = stations[0]
        for i in range(1, n):
            pref_sum[i] = stations[i] + pref_sum[i - 1]

        for i in range(n):
            lft = i - r - 1
            lft_val = pref_sum[lft] if lft >= 0 else 0
            power[i] = pref_sum[min(n - 1, i + r)] - lft_val

        def test(x: int) -> int:
            diff, cur, built_new = [0] * n, 0, 0
            for i in range(n):
                cur += diff[i]
                if (power[i] + cur) >= x:
                    continue
                else:
                    need = x - (power[i] + cur)
                    diff[i] += need
                    cur += need
                    built_new += need
                    if (i + 2 * r + 1) < n:
                        diff[i + 2 * r + 1] -= need
            return built_new

        left, right = min(power), max(power) + k
        while left < right:
            mid = (left + right + 1) // 2
            if test(mid) <= k:
                left = mid
            else:
                right = mid - 1

        return left