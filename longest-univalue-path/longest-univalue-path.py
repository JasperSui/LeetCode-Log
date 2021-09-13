# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.get_len(root, root.val)
        return self.ans
    
    def get_len(self, node, v):
        if not node: return 0
        left = self.get_len(node.left, node.val)
        right = self.get_len(node.right, node.val)
        self.ans = max(self.ans, left + right)
        if v == node.val:
            return max(left, right) + 1
        return 0
        