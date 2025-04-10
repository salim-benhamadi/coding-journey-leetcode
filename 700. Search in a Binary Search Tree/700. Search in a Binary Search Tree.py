from typing import Optional

# Solution 1 : Using Stack
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            
            if node.val == val:
                return node
                
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return None

# Time Complexity : O(n), where n is the number of nodes in the BST
# Space Complexity : O(h), where h is the height of the BST

# Solution 2 : Using Binary Search Tree Properties
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root
        
        while current:
            if current.val == val:
                return current
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        
        return None

# Time Complexity**: O(h), where h is the height of the BST
# Space Complexity**: O(1)