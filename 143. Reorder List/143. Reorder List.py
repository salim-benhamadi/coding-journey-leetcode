from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # Step 1: Find the middle of the linked list
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Split the list and reverse the second half
        second_list = slow.next
        slow.next = None
        
        node = second_list
        previous_node = None

        while node:
            next_node = node.next
            node.next = previous_node
            previous_node = node
            node = next_node
        
        # Step 3: Merge the two lists alternately
        second_list = previous_node
        node = head
        
        while node and second_list:
            tmp = node.next
            tmp2 = second_list.next
            node.next = second_list
            second_list.next = tmp

            node = tmp
            second_list = tmp2


# Time Complexity : O(n), where n is the number of nodes in the linked list
# Space Complexity : O(1)