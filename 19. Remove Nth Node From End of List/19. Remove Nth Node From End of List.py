from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node, length = head, 1
        while node.next:
            node = node.next
            length += 1

        if length - n == 0:
            return head.next
            
        node = head
        for i in range(length - n - 1):
            node = node.next
        node.next = node.next.next
        return head

# Time complexity: O(n)
# Space complexity: O(1)

# 2. One Pass Solution (Optimal)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = second = dummy
        for _ in range(n + 1):
            first = first.next   
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

# Time complexity: O(n)
# Space complexity: O(1)