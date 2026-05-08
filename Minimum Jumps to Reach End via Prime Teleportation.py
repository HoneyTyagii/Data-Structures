# 3629. Minimum Jumps to Reach End via Prime Teleportation

# Medium

# You are given an integer array nums of length n.

# You start at index 0, and your goal is to reach index n - 1.

# From any index i, you may perform one of the following operations:

# Adjacent Step: Jump to index i + 1 or i - 1, if the index is within bounds.
# Prime Teleportation: If nums[i] is a prime number p, you may instantly jump to any index j != i such that nums[j] % p == 0.
# Return the minimum number of jumps required to reach index n - 1.

 

# Example 1:

# Input: nums = [1,2,4,6]

# Output: 2

# Explanation:

# One optimal sequence of jumps is:

# Start at index i = 0. Take an adjacent step to index 1.
# At index i = 1, nums[1] = 2 is a prime number. Therefore, we teleport to index i = 3 as nums[3] = 6 is divisible by 2.
# Thus, the answer is 2.

# Example 2:

# Input: nums = [2,3,4,7,9]

# Output: 2

# Explanation:

# One optimal sequence of jumps is:

# Start at index i = 0. Take an adjacent step to index i = 1.
# At index i = 1, nums[1] = 3 is a prime number. Therefore, we teleport to index i = 4 since nums[4] = 9 is divisible by 3.
# Thus, the answer is 2.

# Example 3:

# Input: nums = [4,6,5,8]

# Output: 3

# Explanation:

# Since no teleportation is possible, we move through 0 → 1 → 2 → 3. Thus, the answer is 3.
 

# Constraints:

# 1 <= n == nums.length <= 105
# 1 <= nums[i] <= 106

class Solution:
    N = 10**6 + 5
    prime = [True] * N
    prime[0] = prime[1] = False
    
    for i in range(2, 1001):
        if prime[i]:
            for j in range(i * i, N, i):
                prime[j] = False

    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        limit = nums[0]
        for c in nums:
            limit = max(limit, c)

        head = [-1] * (limit + 1)
        nxt = [-1] * n
        for i in range(n):
            val = nums[i]
            nxt[i] = head[val]
            head[val] = i

        dp = [-1] * n
        dp[0] = 0
        queue = deque([0])
        seen = set()

        while queue:
            dq = queue.popleft()

            if dq == n - 1:
                return dp[dq]

            right = dq + 1
            if right < n and dp[right] == -1:
                dp[right] = dp[dq] + 1
                queue.append(right)

            left = dq - 1
            if left >= 0 and dp[left] == -1:
                dp[left] = dp[dq] + 1
                queue.append(left)

            val = nums[dq]
            if Solution.prime[val] and val not in seen:
                seen.add(val)
                for i in range(val, limit + 1, val):
                    j = head[i]
                    while j != -1:
                        if dp[j] == -1:
                            dp[j] = dp[dq] + 1
                            queue.append(j)
                        j = nxt[j]
                    head[i] = -1
        return -1