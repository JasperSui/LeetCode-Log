# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Time: O(n)
        # Space: O(height)
        
        if not root or p == root or q == root: return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r: return root
        return l or r
        
        
#         if not root or p == root or q == root: return root
#         l = self.lowestCommonAncestor(root.left, p, q)
#         r = self.lowestCommonAncestor(root.right, p, q)
        
#         if l and r: return root
#         return l or r