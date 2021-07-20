# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node, calc=False):
            if not node: return
            if calc and not node.left and not node.right:
                self.ans += node.val
            dfs(node.left, True)
            dfs(node.right)
        dfs(root)
        return self.ans