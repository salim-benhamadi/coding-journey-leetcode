from typing import Optional

# Solution 1: Two-Pass Approach

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle edge cases
        if not head or not head.next:
            return None
            
        # First pass: count the length of the list
        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        
        # Second pass: find the node before middle and delete middle
        node = head
        for i in range(length):
            if i == length // 2 - 1:
                node.next = node.next.next
                return head
            node = node.next

# Time complexity: O(n)
# Space complexity: O(1)

# Solution 2: Fast and Slow Pointers (One-Pass)

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle edge cases
        if not head or not head.next:
            return None
            
        # Use slow and fast pointers
        slow = head
        fast = head.next.next
        
        # When fast reaches end, slow will be at node before middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Delete the middle node
        slow.next = slow.next.next
        return head

# Time complexity: O(n)
# Space complexity: O(1)