# 234. Palindrome Linked List

# Easy

# Given the head of a singly linked list, return true if it is a 
# palindrome
#  or false otherwise.

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:

# Input: head = [1,2]
# Output: false
 
# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        curr = head
        while curr:
            l.append(curr.val)
            curr = curr.next
        return l == l[::-1]