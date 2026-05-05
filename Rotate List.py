# 61. Rotate List

# Medium

# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:

# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur,n = head, 1
        while cur and cur.next: cur,n = cur.next, n+1
        if  n<2 or k%n==0:  return head
        last,cur = cur,head
        for _ in range(n-k%n -1): cur = cur.next
        last.next,head,cur.next = head, cur.next, None
        return head