# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node, p=None, gp=None):
            if not node: return
            if gp and gp.val % 2 == 0:
                self.ans += node.val
            dfs(node.left, node, p)
            dfs(node.right, node, p)
        dfs(root)
        return self.ans