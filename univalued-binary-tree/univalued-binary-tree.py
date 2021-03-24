# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.v = 100

    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root: return True
        print(root.val, self.v)
        if root.val != self.v and self.v != 100: return False
        else:
            self.v = root.val
            return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
        return self.isUnivalTree(root)