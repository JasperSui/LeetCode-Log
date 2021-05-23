# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.ans = 0
        if not root: return 0
        def dfs(node, is_left=False):
            if not node: return
            dfs(node.left, True)
            if is_left and not node.left and not node.right: self.ans += node.val
            dfs(node.right, False)
        dfs(root)
        return self.ans
            