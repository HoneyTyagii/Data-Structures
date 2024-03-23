# 143. Reorder List

# Medium

# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Example 1:

# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Example 2:

# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
 
# Constraints:

# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        res = ListNode(0)
        res.next = head
        slow = fast = res
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        fast = slow.next
        slow.next = None
        fast = self.reverseTwo(fast)
        slow = res.next
        while fast:
            slowp, fastp = slow.next, fast.next
            slow.next, fast.next = fast, slowp
            slow, fast = slowp, fastp
        return res.next


    def reverseTwo(self, node):
        prev = None
        curr = node
        while curr:
            nextp = curr.next
            curr.next = prev
            prev = curr
            curr = nextp
        return prev