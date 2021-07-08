# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        self.min_d = float('inf')
        def dfs(node, d=1):
            if not node: return
            if not node.left and not node.right:
                self.min_d = min(self.min_d, d)
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        dfs(root)
        return self.min_d if root else 0