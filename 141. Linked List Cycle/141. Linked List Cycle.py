from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# 1. Value Modification Approach
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        while node:
            if node.val == "checked": 
                return True
            node.val = "checked"
            node = node.next
        return False
# Time complexity: O(n)
# Space complexity: O(1)    

# 2. Floyd's Cycle Finding Algorithm (Optimal)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else fast.next
            if slow == fast:
                return True
        return False
# Time complexity: O(n)
# Space complexity: O(1)    
