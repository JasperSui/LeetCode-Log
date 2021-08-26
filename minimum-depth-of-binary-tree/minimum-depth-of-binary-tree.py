# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.min_depth = float('inf')
        def dfs(node, depth=1):
            if not node: return
            if not node.left and not node.right:
                self.min_depth = min(self.min_depth, depth)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root)
        return self.min_depth if self.min_depth != float('inf') else 0