# 92. Reverse Linked List II

# Medium

# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Example 1:

# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]

# Constraints:

# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        values = []                        
        nodes = []                         
        counter = 0
        curr = head
        while curr:
            counter += 1
            if counter >= left and counter <= right:
                values.append(curr.val)     
                nodes.append(curr)          
            curr = curr.next
        for node in nodes:
            node.val = values.pop(-1)     
        return head
    
    # time complexity : O(n)
    # space complexity : O(n)