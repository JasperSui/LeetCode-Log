# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(p, q):
            if not p or not q: return p == q
            if p.val != q.val: return False
            return is_mirror(p.left, q.right) and is_mirror(p.right, q.left)
        return is_mirror(root, root)