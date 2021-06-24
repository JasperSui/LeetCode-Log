# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node, f=None, gf=None):
            if not node: return
            dfs(node.left, node.val, f)
            if gf is not None and gf % 2 == 0: self.ans += node.val
            dfs(node.right, node.val, f)
        dfs(root)
        return self.ans