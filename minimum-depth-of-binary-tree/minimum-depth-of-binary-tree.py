# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        self.level = float('inf')
        def dfs(node, level=1):
            if not node: return
            dfs(node.left, level+1)
            if not node.left and not node.right: self.level = min(self.level, level)
            dfs(node.right, level+1)
        dfs(root)
        return self.level if root else 0