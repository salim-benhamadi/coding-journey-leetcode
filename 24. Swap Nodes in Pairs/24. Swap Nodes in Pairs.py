from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current_node = head
        previous_node = None

        if current_node and current_node.next:
            head = current_node.next
        
        while current_node and current_node.next:
            next_node = current_node.next
            
            # Swap the pair
            current_node.next = next_node.next
            next_node.next = current_node
            
            # Connect with previous part of the list
            if previous_node:
                previous_node.next = next_node
                
            # Move to the next pair
            previous_node = current_node
            current_node = current_node.next
        
        return head

# Time complexity: O(n)
# Space complexity: O(1)