from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        stack = [(root, 1)]
        max_depth = 0
        
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
                
        return max_depth

# Time complexity: O(n), where n is the number of nodes in the tree
# Space complexity: O(n), where h is the height of the tree