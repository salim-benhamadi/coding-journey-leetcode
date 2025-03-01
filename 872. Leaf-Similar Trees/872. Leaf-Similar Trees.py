from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Edge case check
        if not root1 or not root2:
            return False
            
        # Get leaf sequence of first tree
        stack = []
        leaves = []
        current = root1
        
        while current or stack:
            # Traverse to leftmost node
            while current:
                stack.append(current)
                current = current.left
                
            # Process current node
            current = stack.pop()
            
            # If leaf node, add to sequence
            if not current.left and not current.right:
                leaves.append(current.val)
                
            # Move to right subtree
            current = current.right
            
        # Compare with leaf sequence of second tree
        stack = []
        leaf_index = 0
        current = root2
        
        while current or stack:
            # Traverse to leftmost node
            while current:
                stack.append(current)
                current = current.left
                
            # Process current node
            current = stack.pop()
            
            # If leaf node, compare with first tree's sequence
            if not current.left and not current.right:
                if leaf_index >= len(leaves):
                    return False
                if current.val != leaves[leaf_index]:
                    return False
                leaf_index += 1
                
            # Move to right subtree
            current = current.right
            
        # Check if all leaves from first tree were matched
        return leaf_index == len(leaves)
    

 # Time Complexity : O(n + m), where n and m are the number of nodes in the two trees
 # Space Complexity : O(h1 + h2 + l), where h1 and h2 are the heights of the trees and l is the number of leaves