# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.curr = 0
        def dfs(node):
            if not node: return
            dfs(node.right)
            self.curr += node.val
            node.val = self.curr
            dfs(node.left)
        dfs(root)
        return root