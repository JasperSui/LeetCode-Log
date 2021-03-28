# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # Time: O(n)
        # Space: O(height)
        
        # Recursive
        self.ans = 0
        def depth(node):
            if not node: return 0
            l, r = depth(node.left), depth(node.right)
            self.ans = max(self.ans, l+r)
            return 1 + max(l, r)
        depth(root)
        return self.ans