# 3721. Longest Balanced Subarray II

# Hard

# You are given an integer array nums.

# A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.

# Return the length of the longest balanced subarray.

 

# Example 1:

# Input: nums = [2,5,4,3]

# Output: 4

# Explanation:

# The longest balanced subarray is [2, 5, 4, 3].
# It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.
# Example 2:

# Input: nums = [3,2,2,5,4]

# Output: 5

# Explanation:

# The longest balanced subarray is [3, 2, 2, 5, 4].
# It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [3, 5]. Thus, the answer is 5.
# Example 3:

# Input: nums = [1,2,3,2]

# Output: 3

# Explanation:

# The longest balanced subarray is [2, 3, 2].
# It has 1 distinct even number [2] and 1 distinct odd number [3]. Thus, the answer is 3.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
    
        tree_min = [0] * (4 * n)
        tree_max = [0] * (4 * n)
        lazy = [0] * (4 * n)

        last_pos = [-1] * 100002 
        
        max_len = 0
        
        def push(node):
            if lazy[node] != 0:
                val = lazy[node]
                
                lazy[2 * node] += val
                tree_min[2 * node] += val
                tree_max[2 * node] += val
                
                lazy[2 * node + 1] += val
                tree_min[2 * node + 1] += val
                tree_max[2 * node + 1] += val
                
                lazy[node] = 0

        def update(node, start, end, l, r, val):
            if l > end or r < start:
                return
            
            if l <= start and end <= r:
                lazy[node] += val
                tree_min[node] += val
                tree_max[node] += val
                return

            push(node)
            mid = (start + end) // 2
            update(2 * node, start, mid, l, r, val)
            update(2 * node + 1, mid + 1, end, l, r, val)
            
            tree_min[node] = min(tree_min[2 * node], tree_min[2 * node + 1])
            tree_max[node] = max(tree_max[2 * node], tree_max[2 * node + 1])

        def find_first_zero(node, start, end):
            if tree_min[node] > 0 or tree_max[node] < 0:
                return -1
            
            if start == end:
                return start if tree_min[node] == 0 else -1
            
            push(node)
            mid = (start + end) // 2
            
            res = find_first_zero(2 * node, start, mid)
            if res != -1:
                return res
            
            return find_first_zero(2 * node + 1, mid + 1, end)
        
        for r in range(n):
            val = nums[r]
            prev_index = last_pos[val]
            
            diff = 1 if (val & 1) == 0 else -1
            
            update(1, 0, n - 1, prev_index + 1, r, diff)
            
            last_pos[val] = r
            
            l = find_first_zero(1, 0, n - 1)
            
            if l != -1:
                current_len = r - l + 1
                if current_len > max_len:
                    max_len = current_len
                    
        return max_len