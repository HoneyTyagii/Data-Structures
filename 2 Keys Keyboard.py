# 650. 2 Keys Keyboard

# Medium

# There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

# Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
# Paste: You can paste the characters which are copied last time.
# Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen. 

# Example 1:

# Input: n = 3
# Output: 3
# Explanation: Initially, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.

# Example 2:

# Input: n = 1
# Output: 0 

# Constraints:

# 1 <= n <= 1000

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        self.target_length = n
        def find_min_steps(current_length: int, clipboard_length: int) -> int:
            if current_length == self.target_length:
                return 0
            if current_length > self.target_length:
                return float('inf')
            copy_and_paste = 2 + find_min_steps(current_length * 2, current_length)
            paste_only = 1 + find_min_steps(current_length + clipboard_length, clipboard_length)
            return min(copy_and_paste, paste_only)
        return 1 + find_min_steps(1, 1)