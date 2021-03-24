# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.v = None

    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root: return True
        if self.v and root.val != self.v: return False
        else:
            self.v = root.val
            return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
        return self.isUnivalTree(root)