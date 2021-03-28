# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        # Time: O(n)
        # Space: O(height)
        
        # Recursive
        self.ans = 0
        def depth(node):
            if not node: return 0
            l_len, r_len = depth(node.left), depth(node.right)
            l = l_len + 1 if node.left and node.left.val == node.val else 0
            r = r_len + 1 if node.right and node.right.val == node.val else 0
            self.ans = max(self.ans, l+r)
            return max(l, r)
        depth(root)
        return self.ans