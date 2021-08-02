# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.ans = 0
        def dfs(node):
            if not node: return
            if node.val < L: dfs(node.right)
            if node.val > R: dfs(node.left)
            if L <= node.val <= R:
                dfs(node.left)
                dfs(node.right)
                self.ans += node.val
        dfs(root)
        return self.ans