# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        self.min_depth = 50000000
        if not root: return 0
        def dfs(node, depth):
            if node:
                temp_depth = depth + 1
                if not node.left and not node.right:
                    self.min_depth = min(self.min_depth, temp_depth)
                dfs(node.left, temp_depth)
                dfs(node.right, temp_depth)
        dfs(root, 0)
        return self.min_depth
        