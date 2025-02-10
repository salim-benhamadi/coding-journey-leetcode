from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
            
        sortedlist = ListNode()
        head = sortedlist
        
        while list1 and list2:
            if list1.val <= list2.val:
                sortedlist.next = list1
                list1 = list1.next
                sortedlist = sortedlist.next
                sortedlist.next = None  
            else:
                sortedlist.next = list2
                list2 = list2.next
                sortedlist = sortedlist.next
                sortedlist.next = None  
        
        if list1: sortedlist.next = list1
        if list2: sortedlist.next = list2
            
        return head.next
    
# Time complexity: O(n + m) where n and m are the lengths of list1 and list2 respectively
# Space complexity: O(1)