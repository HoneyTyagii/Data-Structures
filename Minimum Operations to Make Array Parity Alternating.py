# Q3. Minimum Operations to Make Array Parity Alternating

# Medium

# You are given an integer array nums.
# An array is parity alternating if for every index i (0 <= i < n-1),
# nums[i] and nums[i+1] have different parity.
# In one operation, choose any index and increase or decrease nums[i] by 1.
# Return [min_ops, min_range] where min_range is the minimum max-min
# over all parity alternating arrays achievable with exactly min_ops operations.

from typing import List


class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return [0, 0]

        merunavilo = nums[:]

        def solve(pattern: int):
            """
            pattern=0: even at even indices, odd at odd indices
            pattern=1: odd at even indices, even at odd indices
            Returns (cost, min_range).
            """
            fixed = []
            flexible = []
            cost = 0

            for i in range(n):
                target_parity = (i + pattern) % 2
                if nums[i] % 2 == target_parity:
                    fixed.append(nums[i])
                else:
                    cost += 1
                    # changing by +1 or -1 flips parity; both options are valid
                    flexible.append((nums[i] - 1, nums[i] + 1))

            # Find the minimum-length interval [lo, hi] that contains every
            # fixed value and at least one option from each flexible pair.
            # This is a classic "smallest window covering all groups" problem.
            events = []  # (value, element_id)
            eid = 0
            for v in fixed:
                events.append((v, eid))
                eid += 1
            for a, b in flexible:
                events.append((a, eid))
                events.append((b, eid))
                eid += 1

            total = eid
            events.sort()

            # Sliding window
            count = [0] * total
            covered = 0
            best = float('inf')
            left = 0

            for right in range(len(events)):
                r_id = events[right][1]
                if count[r_id] == 0:
                    covered += 1
                count[r_id] += 1

                while covered == total:
                    best = min(best, events[right][0] - events[left][0])
                    l_id = events[left][1]
                    count[l_id] -= 1
                    if count[l_id] == 0:
                        covered -= 1
                    left += 1

            return cost, best

        cost_e, range_e = solve(0)
        cost_o, range_o = solve(1)

        if cost_e < cost_o:
            return [cost_e, range_e]
        elif cost_o < cost_e:
            return [cost_o, range_o]
        else:
            return [cost_e, min(range_e, range_o)]
